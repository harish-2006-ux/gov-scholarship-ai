from flask import Flask, request, jsonify, render_template, session, redirect, url_for, flash
from models import Session, Scholarship, User, Application, Base, engine
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = "scholarship_portal_secret_key_2024"

# Email Configuration (SMTP) - UPDATE THESE WITH YOUR EMAIL SETTINGS
# For Gmail: Use App Password (not your regular password)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-email@gmail.com"  # Change this to your email
SMTP_PASSWORD = "your-app-password"  # Change this to your app password
FROM_EMAIL = "your-email@gmail.com"  # Change this to your email

def send_email(to_email, subject, body):
    """Send an email using SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

def send_welcome_email(user_email, user_name):
    """Send welcome email after successful registration"""
    subject = "Welcome to Karnataka Scholarship Portal!"
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2 style="color: #4CAF50;">Welcome to Karnataka Scholarship Portal, {user_name}!</h2>
        <p>Your account has been successfully created.</p>
        <p>You can now:</p>
        <ul>
            <li>Browse and search for scholarships</li>
            <li>Apply for eligible scholarships</li>
            <li>Track your application status</li>
            <li>Connect your DigiLocker for document verification</li>
        </ul>
        <p>Start exploring scholarships now: <a href="http://127.0.0.1:5000/">Karnataka Scholarship Portal</a></p>
        <br>
        <p>Best regards,<br>Karnataka Scholarship Portal Team</p>
    </body>
    </html>
    """
    send_email(user_email, subject, body)

def send_application_confirmation(user_email, user_name, scholarship_name):
    """Send confirmation email after successful scholarship application"""
    subject = f"Scholarship Application Submitted - {scholarship_name}"
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2 style="color: #2196F3;">Scholarship Application Submitted!</h2>
        <p>Dear {user_name},</p>
        <p>Your application for <strong>{scholarship_name}</strong> has been submitted successfully.</p>
        <h3>Application Details:</h3>
        <ul>
            <li><strong>Scholarship:</strong> {scholarship_name}</li>
            <li><strong>Status:</strong> Applied</li>
            <li><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</li>
        </ul>
        <h3>What happens next?</h3>
        <p>Your application is now under review. You will receive updates on:</p>
        <ul>
            <li>Document verification status</li>
            <li>Application approval/rejection</li>
            <li>Scholarship disbursement</li>
        </ul>
        <p>Track your application: <a href="http://127.0.0.1:5000/profile">My Profile</a></p>
        <br>
        <p>Best regards,<br>Karnataka Scholarship Portal Team</p>
    </body>
    </html>
    """
    send_email(user_email, subject, body)

def send_scholarship_approved(user_email, user_name, scholarship_name):
    """Send notification when scholarship is approved"""
    subject = f"Scholarship Approved - {scholarship_name}!"
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2 style="color: #4CAF50;">Congratulations! Your Scholarship Has Been Approved!</h2>
        <p>Dear {user_name},</p>
        <p>We are pleased to inform you that your application for <strong>{scholarship_name}</strong> has been approved!</p>
        <h3>Approved Scholarship Details:</h3>
        <ul>
            <li><strong>Scholarship:</strong> {scholarship_name}</li>
            <li><strong>Status:</strong> Approved</li>
            <li><strong>Approval Date:</strong> {datetime.now().strftime('%Y-%m-%d')}</li>
        </ul>
        <h3>Next Steps:</h3>
        <ol>
            <li>Check your registered bank account for scholarship disbursement</li>
            <li>Keep your DigiLocker documents updated</li>
            <li>Regularly check your profile for any updates</li>
        </ol>
        <p>View your awarded scholarships: <a href="http://127.0.0.1:5000/profile">My Profile</a></p>
        <br>
        <p>Best regards,<br>Karnataka Scholarship Portal Team</p>
    </body>
    </html>
    """
    send_email(user_email, subject, body)

# Create database tables
Base.metadata.create_all(engine)

# -------------------------------
# Eligibility Logic
# -------------------------------
def check_eligibility(user_profile, scholarship):
    # Get user data from profile or request
    if hasattr(user_profile, 'age'):
        age = user_profile.age
        income = user_profile.income
        caste = user_profile.caste
        gender = user_profile.gender
        course = user_profile.course
        district = user_profile.district
    else:
        age = user_profile.get("age")
        income = user_profile.get("income")
        caste = user_profile.get("caste")
        gender = user_profile.get("gender")
        course = user_profile.get("course")
        district = user_profile.get("district")

    # Age
    if not (scholarship.min_age <= age <= scholarship.max_age):
        return None

    # Income
    if income > scholarship.max_income:
        return None

    # Course
    # Handle "School" course (for Pre-Matric scholarships)
    # Also handle "Both" which means both PUC and Degree (but not School)
    if scholarship.course_allowed == "School":
        if course != "School":
            return None
    elif scholarship.course_allowed != "Both":
        if course != scholarship.course_allowed:
            return None
    # If scholarship.course_allowed is "Both", it applies to PUC and Degree, not School

    # Caste
    if scholarship.caste_allowed != "Any":
        allowed_castes = [c.strip() for c in scholarship.caste_allowed.split(",")]
        if caste not in allowed_castes:
            return None
    
    # District
    if scholarship.district_allowed != "All":
        allowed_districts = [d.strip() for d in scholarship.district_allowed.split(",")]
        if district not in allowed_districts:
            return None

    # Score calculation
    score = 4
    if scholarship.gender_allowed == "Any" or gender == scholarship.gender_allowed:
        score += 1

    return score

# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    user_logged_in = 'user_id' in session
    return render_template("index.html", user_logged_in=user_logged_in)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    db_session = Session()
    
    try:
        # Check if email exists
        existing_user = db_session.query(User).filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({"success": False, "message": "Email already registered"}), 400
        
        # Create new user
        user = User(
            first_name=data['first_name'],
            last_name=data.get('last_name', ''),
            email=data['email'],
            phone=data.get('phone', ''),
            password_hash=generate_password_hash(data['password']),
            date_of_birth=datetime.strptime(data['dob'], '%Y-%m-%d') if data.get('dob') else None,
            gender=data.get('gender', ''),
            caste=data.get('caste', ''),
            district=data.get('district', '')
        )
        db_session.add(user)
        db_session.commit()
        
        # Send welcome email
        send_welcome_email(data['email'], data['first_name'])
        
        return jsonify({"success": True, "message": "Account created successfully!"})
    except Exception as e:
        db_session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db_session.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    db_session = Session()
    
    try:
        user = db_session.query(User).filter_by(email=data['email']).first()
        
        if user and check_password_hash(user.password_hash, data['password']):
            session['user_id'] = user.id
            session['user_name'] = user.first_name
            session['user_email'] = user.email
            return jsonify({"success": True, "message": "Login successful!"})
        else:
            return jsonify({"success": False, "message": "Invalid email or password"}), 401
    finally:
        db_session.close()

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/profile")
def profile():
    if 'user_id' not in session:
        return redirect(url_for('signup'))
    
    db_session = Session()
    try:
        user = db_session.query(User).filter_by(id=session['user_id']).first()
        if not user:
            return redirect(url_for('signup'))
        
        # Get applications
        applications = db_session.query(Application).filter_by(user_id=user.id).all()
        
        applied_scholarships = []
        awarded_scholarships = []
        
        for app in applications:
            scholarship = db_session.query(Scholarship).filter_by(id=app.scholarship_id).first()
            if scholarship:
                app_data = {
                    'id': app.id,
                    'scholarship_name': scholarship.name,
                    'status': app.status,
                    'application_date': app.application_date.strftime('%Y-%m-%d') if app.application_date else 'N/A',
                    'documents_verified': app.documents_verified,
                    'notes': app.notes
                }
                if app.status == "Approved":
                    awarded_scholarships.append(app_data)
                else:
                    applied_scholarships.append(app_data)
        
        return render_template("profile.html", 
                             user=user, 
                             applied_scholarships=applied_scholarships,
                             awarded_scholarships=awarded_scholarships)
    finally:
        db_session.close()

@app.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('signup'))
    
    db_session = Session()
    try:
        user = db_session.query(User).filter_by(id=session['user_id']).first()
        if not user:
            return redirect(url_for('signup'))
        
        if request.method == "POST":
            data = request.form
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.phone = data.get('phone', user.phone)
            user.gender = data.get('gender', user.gender)
            user.caste = data.get('caste', user.caste)
            user.district = data.get('district', user.district)
            if data.get('dob'):
                user.date_of_birth = datetime.strptime(data['dob'], '%Y-%m-%d')
            db_session.commit()
            flash("Profile updated successfully!", "success")
            return redirect(url_for('profile'))
        
        return render_template("edit_profile.html", user=user)
    finally:
        db_session.close()

@app.route("/digilocker/connect")
def digilocker_connect():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Please login first"}), 401
    
    db_session = Session()
    try:
        user = db_session.query(User).filter_by(id=session['user_id']).first()
        user.digilocker_linked = True
        user.digilocker_id = "DigiLocker_" + str(user.id)
        db_session.commit()
        return jsonify({"success": True, "message": "DigiLocker connected successfully!"})
    finally:
        db_session.close()

@app.route("/digilocker/disconnect")
def digilocker_disconnect():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Please login first"}), 401
    
    db_session = Session()
    try:
        user = db_session.query(User).filter_by(id=session['user_id']).first()
        user.digilocker_linked = False
        user.digilocker_id = None
        db_session.commit()
        return jsonify({"success": True, "message": "DigiLocker disconnected"})
    finally:
        db_session.close()

@app.route("/apply/<int:scholarship_id>", methods=["POST"])
def apply_scholarship(scholarship_id):
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Please login to apply"}), 401
    
    db_session = Session()
    try:
        # Check if already applied
        existing = db_session.query(Application).filter_by(
            user_id=session['user_id'], 
            scholarship_id=scholarship_id
        ).first()
        
        if existing:
            return jsonify({"success": False, "message": "Already applied for this scholarship"}), 400
        
        # Check eligibility
        user = db_session.query(User).filter_by(id=session['user_id']).first()
        scholarship = db_session.query(Scholarship).filter_by(id=scholarship_id).first()
        
        if not scholarship:
            return jsonify({"success": False, "message": "Scholarship not found"}), 404
        
        # Create application
        application = Application(
            user_id=session['user_id'],
            scholarship_id=scholarship_id,
            status="Applied"
        )
        db_session.add(application)
        db_session.commit()
        
        # Send confirmation email
        user_name = user.first_name or "User"
        send_application_confirmation(user.email, user_name, scholarship.name)
        
        return jsonify({"success": True, "message": "Application submitted successfully!"})
    except Exception as e:
        db_session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db_session.close()

@app.route("/approve/<int:application_id>", methods=["POST"])
def approve_application(application_id):
    """Admin route to approve a scholarship application - sends email notification"""
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Please login first"}), 401
    
    db_session = Session()
    try:
        application = db_session.query(Application).filter_by(id=application_id).first()
        if not application:
            return jsonify({"success": False, "message": "Application not found"}), 404
        
        user = db_session.query(User).filter_by(id=application.user_id).first()
        scholarship = db_session.query(Scholarship).filter_by(id=application.scholarship_id).first()
        
        if not user or not scholarship:
            return jsonify({"success": False, "message": "User or scholarship not found"}), 404
        
        # Update status
        application.status = "Approved"
        db_session.commit()
        
        # Send approval email
        user_name = user.first_name or "User"
        send_scholarship_approved(user.email, user_name, scholarship.name)
        
        return jsonify({"success": True, "message": "Application approved and notification sent!"})
    except Exception as e:
        db_session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db_session.close()

@app.route("/recommend", methods=["POST"])
def recommend():
    user_data = request.json

    # If user is logged in, get their profile data
    if 'user_id' in session:
        db_session = Session()
        try:
            user = db_session.query(User).filter_by(id=session['user_id']).first()
            if user:
                user_data['age'] = user_data.get('age') or calculate_age(user.date_of_birth) if user.date_of_birth else 18
                user_data['caste'] = user_data.get('caste') or user.caste or "General"
                user_data['gender'] = user_data.get('gender') or user.gender or "Male"
                user_data['district'] = user_data.get('district') or user.district or "Bangalore Urban"
                user_data['course'] = user_data.get('course') or "Degree"
                user_data['income'] = user_data.get('income') or 250000
        finally:
            db_session.close()
    
    db_session = Session()
    scholarships = db_session.query(Scholarship).all()
    results = []

    for scheme in scholarships:
        score = check_eligibility(user_data, scheme)

        if score is not None:
            # Check if user already applied
            already_applied = False
            if 'user_id' in session:
                existing = db_session.query(Application).filter_by(
                    user_id=session['user_id'],
                    scholarship_id=scheme.id
                ).first()
                already_applied = existing is not None

            results.append({
                "id": scheme.id,
                "name": scheme.name,
                "score": score,
                "description": scheme.description,
                "documents": scheme.required_documents,
                "url": scheme.official_url,
                "portal": "Karnataka" if scheme.official_url and "karnataka" in scheme.official_url.lower() else "National",
                "already_applied": already_applied
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return jsonify(results)

def calculate_age(birth_date):
    if birth_date:
        today = datetime.now()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return 18

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
