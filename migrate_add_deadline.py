# Migration script to add deadline column to scholarships table
import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if deadline column exists
cursor.execute("PRAGMA table_info(scholarships)")
columns = [col[1] for col in cursor.fetchall()]

if 'deadline' not in columns:
    print("Adding 'deadline' column to scholarships table...")
    cursor.execute("ALTER TABLE scholarships ADD COLUMN deadline TIMESTAMP")
    conn.commit()
    print("Column added successfully!")
else:
    print("Column 'deadline' already exists.")

conn.close()
print("Migration complete!")
