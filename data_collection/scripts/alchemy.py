import psycopg2

conn = psycopg2.connect(
host="localhost",
database="your_database",
user="your_user",
password="your_password")
cursor = conn.cursor()

cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)

tables = cursor.fetchall()
print(tables)

conn.commit()
cursor.close()
conn.close()