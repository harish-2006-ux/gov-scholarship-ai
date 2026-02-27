#!/usr/bin/env python3
"""
Simple Database Viewer for Karnataka Scholarship Portal
Run this script to view all data in the database
"""

import sqlite3

def view_scholarships(conn):
    """View all scholarships"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, caste_allowed, gender_allowed, course_allowed, 
               max_income, official_url 
        FROM scholarships 
        ORDER BY id
    """)
    rows = cursor.fetchall()
    
    print("\n" + "="*80)
    print("📚 SCHOLARSHIPS (Total: " + str(len(rows)) + ")")
    print("="*80)
    
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Caste: {row[2]}")
        print(f"Gender: {row[3]}")
        print(f"Course: {row[4]}")
        print(f"Max Income: ₹{row[5]:,.0f}")
        print(f"URL: {row[6]}")

def view_users(conn):
    """View all users"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, first_name, last_name, email, phone, gender, caste, district, income, course
        FROM users 
        ORDER BY id
    """)
    rows = cursor.fetchall()
    
    print("\n" + "="*80)
    print("👥 USERS (Total: " + str(len(rows)) + ")")
    print("="*80)
    
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"Name: {row[1]} {row[2]}")
        print(f"Email: {row[3]}")
        print(f"Phone: {row[4]}")
        print(f"Gender: {row[5]}")
        print(f"Caste: {row[6]}")
        print(f"District: {row[7]}")
        print(f"Income: ₹{row[8]:,.0f}" if row[8] else "Income: N/A")
        print(f"Course: {row[9]}")

def view_applications(conn):
    """View all applications"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, u.email, s.name, a.status, a.application_date, a.documents_verified
        FROM applications a
        JOIN users u ON a.user_id = u.id
        JOIN scholarships s ON a.scholarship_id = s.id
        ORDER BY a.id
    """)
    rows = cursor.fetchall()
    
    print("\n" + "="*80)
    print("📝 APPLICATIONS (Total: " + str(len(rows)) + ")")
    print("="*80)
    
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"User: {row[1]}")
        print(f"Scholarship: {row[2]}")
        print(f"Status: {row[3]}")
        print(f"Date: {row[4]}")
        print(f"Docs Verified: {'Yes' if row[5] else 'No'}")

def view_visits(conn):
    """View all visits"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.id, u.email, v.visit_date, v.page, v.action
        FROM visits v
        LEFT JOIN users u ON v.user_id = u.id
        ORDER BY v.id DESC
        LIMIT 20
    """)
    rows = cursor.fetchall()
    
    print("\n" + "="*80)
    print("👁️ RECENT VISITS (Last 20)")
    print("="*80)
    
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"User: {row[1] or 'Anonymous'}")
        print(f"Date: {row[2]}")
        print(f"Page: {row[3]}")
        print(f"Action: {row[4]}")

def main():
    try:
        conn = sqlite3.connect('database.db')
        
        print("\n" + "🎓 " * 20)
        print("KARNATAKA SCHOLARSHIP PORTAL - DATABASE VIEWER")
        print("🎓 " * 20)
        
        view_scholarships(conn)
        view_users(conn)
        view_applications(conn)
        view_visits(conn)
        
        print("\n" + "="*80)
        print("✅ Database viewing complete!")
        print("="*80)
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
