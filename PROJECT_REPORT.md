# Karnataka Scholarship Portal - Complete Project Report

## 📋 Project Overview

**Project Name:** Karnataka Scholarship Portal  
**Type:** Web Application (Flask + SQLite)  
**Purpose:** A scholarship discovery and eligibility checking portal for students in Karnataka, India  
**Target Users:** Students seeking government scholarships (School, PUC, Undergraduate, Postgraduate, PhD)

---

## 🏗️ Architecture

### Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend** | Flask | 3.1.3 |
| **Database** | SQLite + SQLAlchemy | 2.0.46 |
| **Frontend** | HTML5, CSS3, JavaScript | - |
| **Charts** | Chart.js | Latest |
| **Deployment** | Gunicorn | 25.1.0 |

### Project Structure

```
gov-scholarship-ai/
├── app.py                  # Main Flask application
├── models.py               # Database models (SQLAlchemy)
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version
├── Procfile                # Deployment config
├── database.db             # SQLite database
│
├── templates/              # HTML templates
│   ├── index.html          # Home page (scholarship search)
│   ├── signup.html         # User registration
│   ├── profile.html        # User profile & applications
│   ├── edit_profile.html   # Edit profile
│   ├── stats.html          # Statistics dashboard
│   ├── competencies.html   # Skills tracking
│   └── signup_new.html     # Alternative signup
│
├── static/                 # Static files
│   └── style.css           # Main stylesheet
│
├── scripts/                # Utility scripts
│   ├── insert_scholarships.py     # Insert scholarship data
│   ├── insert_ssp_scholarships.py # Insert SSP scholarships
│   ├── insert_all_courses.py      # Insert all course scholarships
│   ├── clear_data.py              # Clear database
│   ├── add_sample_data.py        # Add sample data
│   ├── show_db.py                # Display database contents
│   └── check_courses.py          # Check courses
│
└── .git/                  # Git repository
```

---

## 📦 Dependencies (requirements.txt)

```
Flask==3.1.3              # Web framework
SQLAlchemy==2.0.46        # ORM
Werkzeug==3.1.6          # Password hashing
Jinja2==3.1.6             # Template engine
gunicorn==25.1.0          # WSGI server
matplotlib==3.10.0        # Data visualization
pandas==2.2.3             # Data analysis
authlib==1.3.2            # OAuth authentication
requests==2.32.3          # HTTP requests
blinker==1.9.0            # Flask extensions
click==8.3.1              # CLI commands
colorama==0.4.6           # Terminal colors
packaging==26.0           # Package utilities
```

---

## 🗄️ Database Schema

### Tables

#### 1. **Scholarships**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment ID |
| name | String(255) | Scholarship name |
| description | Text | Scholarship details |
| min_age | Integer | Minimum eligible age |
| max_age | Integer | Maximum eligible age |
| max_income | Float | Maximum annual income |
| caste_allowed | String(100) | Eligible castes |
| gender_allowed | String(50) | Gender restriction |
| course_allowed | String(50) | School/PUC/Degree/PG/PhD |
| district_allowed | String(100) | Eligible districts |
| required_documents | Text | Documents needed |
| official_url | String(500) | Application portal link |

#### 2. **Users**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment ID |
| first_name | String(100) | First name |
| last_name | String(100) | Last name |
| email | String(255) | Unique email |
| phone | String(20) | Phone number |
| password_hash | String(255) | Hashed password |
| date_of_birth | DateTime | DOB |
| gender | String(20) | Male/Female/Other |
| caste | String(50) | Caste category |
| district | String(100) | Karnataka district |
| income | Float | Annual income |
| course | String(50) | Current course |
| created_at | DateTime | Registration date |

#### 3. **Applications**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment ID |
| user_id | Integer (FK) | Reference to User |
| scholarship_id | Integer (FK) | Reference to Scholarship |
| status | String(50) | Applied/Awaiting/Approved/Rejected |
| application_date | DateTime | Submission date |
| documents_verified | Boolean | Verification status |
| notes | Text | Additional notes |

#### 4. **Visits**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment ID |
| user_id | Integer (FK) | Reference to User |
| visit_date | DateTime | Visit timestamp |
| page | String(100) | Page visited |
| action | String(100) | Action performed |

---

## 🌐 API Endpoints

### Pages
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/signup` | GET | Registration page |
| `/register` | POST | Register new user |
| `/login` | POST | User login |
| `/logout` | GET | User logout |
| `/profile` | GET | User profile |
| `/profile/edit` | GET/POST | Edit profile |
| `/apply/<id>` | POST | Apply for scholarship |
| `/approve/<id>` | POST | Approve application (admin) |
| `/stats` | GET | Statistics dashboard |

### JSON APIs
| Route | Method | Description |
|-------|--------|-------------|
| `/recommend` | POST | Get eligible scholarships |
| `/api/stats/summary` | GET | Dashboard summary |
| `/api/stats/scholarships` | GET | Scholarship statistics |
| `/api/stats/users` | GET | User statistics |
| `/api/stats/applications` | GET | Application statistics |
| `/api/stats/applications-by-user` | GET | Applications per user |

---

## 📊 Features

### 1. Scholarship Search
- Filter by: Age, Income, Caste, Gender, Course, District
- Eligibility scoring (S/A/B/C ranks)
- Direct links to official portals

### 2. User Management
- Registration with email verification
- Login/Logout
- Profile management
- Password hashing (Werkzeug)

### 3. Application Tracking
- Apply for scholarships
- Track application status
- Document verification status

### 4. Statistics Dashboard
- Total scholarships, users, applications
- Charts: Applications by status, Scholarships by course, Users by gender/district
- Real database data (no random values)

### 5. Email Notifications (SMTP)
- Welcome email on registration
- Application confirmation
- Approval notifications

---

## 🎓 Scholarship Database

### Total: 53 Real Scholarships

| Course Level | Count | Examples |
|--------------|-------|----------|
| **School** | 7 | Pre-Matric SC/ST/OBC, PM YASASVI |
| **PUC** | 6 | Post-Matric SC/ST/OBC, Vidyasiri |
| **Undergraduate** | 16 | Degree College, Professional Courses |
| **Postgraduate** | 8 | Masters programs, AICTE PG |
| **PhD** | 8 | UGC NET JRF, CSIR NET, INSPIRE |
| **Vocational** | 3 | ITI, Polytechnic |
| **Both** | 5 | Minority, Special categories |

### Scholarship Sources
- **SSP** (Student Scholarship Portal) - Karnataka
- **NSP** (National Scholarship Portal) - Central
- **PM YASASVI** - Prime Minister's scheme
- **AICTE** - Technical education
- **State Schemes** - Karnataka government

---

## 🚀 Running the Project

### 1. Install Dependencies
```
bash
pip install -r requirements.txt
```

### 2. Initialize Database
```
bash
python insert_all_courses.py
```

### 3. Run Application
```
bash
python app.py
```

### 4. Access
```
http://127.0.0.1:5000
```

### 5. View Statistics
```
http://127.0.0.1:5000/stats
```

---

## 📱 Key Features Summary

✅ Scholarship search with eligibility filtering  
✅ User registration and authentication  
✅ Profile management  
✅ Scholarship application tracking  
✅ Statistics dashboard with real data  
✅ Email notifications  
✅ Mobile-responsive design  
✅ 53 real Karnataka government scholarships  
✅ Multiple course levels supported  

---

## 🔧 Configuration

### Email Settings (app.py)
```
python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-email@gmail.com"
SMTP_PASSWORD = "your-app-password"
FROM_EMAIL = "your-email@gmail.com"
```

### Database
- Type: SQLite
- Location: `database.db`
- ORM: SQLAlchemy

---

## 📄 License

This project is for educational purposes. Scholarship data is sourced from official Karnataka government portals.

---

**Report Generated:** February 2026  
**Project Version:** 1.0
