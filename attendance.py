import sqlite3

conn = sqlite3.connect("attendance.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS attendance(
                   r_no INTEGER PRIMARY KEY,
                   attended_hours INTEGER,
                   total_hours INTEGER,
                   percentage REAL GENERATED ALWAYS AS 
                   (attended_hours * 100.0 / total_hours)
               )
               """)

students = [
    (23,351,448),
    (39,391,448),
    (2,391,448),
    (59,331,448),
    (27,361,448),
    (28,374,448),
    (41,276,448),
    (34,349,448)
]
cursor.executemany("INSERT INTO attendance(r_no,attended_hours,total_hours) values (?,?,?)",students)
conn.commit()
conn.close()