import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('SELECT course_allowed, COUNT(*) FROM scholarships GROUP BY course_allowed')
rows = cursor.fetchall()
print('=== SCHOLARSHIPS BY COURSE LEVEL ===\n')
for r in rows:
    print(f'{r[0]}: {r[1]} scholarships')
conn.close()
