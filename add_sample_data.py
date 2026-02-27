"""
Script to add sample users and applications for testing the statistics dashboard
"""
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Sample users with different districts (Karnataka districts)
sample_users = [
    ('Rahul', 'Sharma', 'rahul.sharma@example.com', 'Male', 'General', 'Bangalore Urban'),
    ('Priya', 'Patel', 'priya.patel@example.com', 'Female', 'OBC', 'Mysuru'),
    ('Amith', 'Kumar', 'amith.kumar@example.com', 'Male', 'SC', 'Tumakuru'),
    ('Sneha', 'Reddy', 'sneha.reddy@example.com', 'Female', 'ST', 'Dakshina Kannada'),
    ('Vikram', 'Singh', 'vikram.singh@example.com', 'Male', 'OBC', 'Hubli-Dharwad'),
    ('Lakshmi', 'Devi', 'lakshmi.devi@example.com', 'Female', 'SC', 'Belagavi'),
    ('Raj', 'Nair', 'raj.nair@example.com', 'Male', 'General', 'Mangalore'),
    ('Divya', 'Iyer', 'divya.iyer@example.com', 'Female', 'OBC', 'Bangalore Rural'),
    ('Kiran', 'Joshi', 'kiran.joshi@example.com', 'Male', 'ST', 'Mysuru'),
    ('Anjali', 'Rao', 'anjali.rao@example.com', 'Female', 'General', 'Tumakuru'),
]

print("Adding sample users...")
for first_name, last_name, email, gender, caste, district in sample_users:
    # Generate a simple password hash (for testing only)
    password_hash = 'scrypt:32768:8:1$test$test_hash'
    
    cursor.execute("""
        INSERT INTO users (first_name, last_name, email, phone, password_hash, date_of_birth, gender, caste, district, income, course, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (first_name, last_name, email, '9876543210', password_hash, '2005-01-01', gender, caste, district, 150000, 'Degree', datetime.now(), datetime.now()))

conn.commit()
print(f"Added {len(sample_users)} users")

# Get user IDs
cursor.execute("SELECT id, first_name FROM users WHERE id > 3")
users = cursor.fetchall()
print(f"Total users now: {len(users)}")

# Add sample applications
print("\nAdding sample applications...")
sample_applications = []
for user in users[:5]:  # First 5 users apply
    user_id = user[0]
    # Each user applies to 1-3 scholarships
    import random
    num_apps = random.randint(1, 3)
    scholarship_ids = random.sample([1, 2, 3, 4, 5], min(num_apps, 5))
    for sch_id in scholarship_ids:
        status = random.choice(['Applied', 'Applied', 'Applied', 'Approved', 'Pending'])
        sample_applications.append((user_id, sch_id, status, datetime.now()))

for user_id, scholarship_id, status, app_date in sample_applications:
    cursor.execute("""
        INSERT INTO applications (user_id, scholarship_id, status, application_date, documents_verified)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, scholarship_id, status, app_date, random.choice([True, False])))

conn.commit()
print(f"Added {len(sample_applications)} applications")

# Display summary
print("\n=== Database Summary ===")
cursor.execute("SELECT COUNT(*) FROM users")
print(f"Total Users: {cursor.fetchone()[0]}")

cursor.execute("SELECT district, COUNT(*) FROM users GROUP BY district")
print("\nUsers by District:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

cursor.execute("SELECT COUNT(*) FROM applications")
print(f"\nTotal Applications: {cursor.fetchone()[0]}")

cursor.execute("SELECT status, COUNT(*) FROM applications GROUP BY status")
print("\nApplications by Status:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

conn.close()
print("\nDone! Refresh the stats page to see the charts populated.")
