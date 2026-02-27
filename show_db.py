import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables in database.db:")
for table in tables:
    print(f"- {table[0]}")

# Show sample data for each table
for table in tables:
    table_name = table[0]
    print(f"\n{table_name} (first 5 rows):")
    try:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data")
    except Exception as e:
        print(f"Error: {e}")

conn.close()
