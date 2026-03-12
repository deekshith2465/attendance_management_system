import sqlite3

conn = sqlite3.connect("Attendance.db")

cursor = conn.cursor()

cursor.execute("""
               SELECT * FROM attendance""")

data = cursor.fetchall()
print("Data in table :",data)
conn.close()