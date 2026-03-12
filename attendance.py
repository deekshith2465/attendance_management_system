import sqlite3

conn = sqlite3.connect("Attendance.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS attendance(
                   r_no INTEGER,
                   attended_hours INTEGER,
                   total_hours INTEGER,
                   percentage REAL)""")

students = [
    (11,270,413,65.2),
    (34,314,413,76.02),
    (59,310,413,75.06),
    (28,339,413,82.08),
    (39,356,413,86.19),
    (2,356,413,86.19),
    (41,248,413,60.04),
    (27,347,413,84.01)
]
cursor.executemany(
    "INSERT INTO attendance(r_no,attended_hours,total_hours,percentage) values (?,?,?,?)",
    students)

print("Table Created Successfully")
conn.commit()
conn.close()