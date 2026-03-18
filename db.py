import psycopg2
import os

conn = psycopg2.connect("postgresql://attendance_db_tezb_user:iO8Xaub1Z0g98jtTkyKb1ZD9U3mxwGmi@dpg-d6rsnup4tr6s73aajk40-a.oregon-postgres.render.com/attendance_db_tezb")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    r_no INTEGER PRIMARY KEY,
    attended_hours INTEGER,
    total_hours INTEGER,
    percentage NUMERIC(5,2) GENERATED ALWAYS AS (
        (attended_hours * 100.0) / NULLIF(total_hours,0)
    ) STORED
);
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
cursor.executemany(
"INSERT INTO attendance (r_no, attended_hours, total_hours) VALUES (%s,%s,%s) ON CONFLICT (r_no) DO NOTHING",
students
)

conn.commit()
