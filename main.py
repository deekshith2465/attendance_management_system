
import sqlite3

conn = sqlite3.connect("Attendance.db", check_same_thread=False)

cursor = conn.cursor()

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/details/{rno}")
def attendance_view(rno : int):
    cursor.execute("""
                   SELECT attended_hours,total_hours,
                   percentage FROM attendance WHERE r_no = ? """,(rno,))
    result = cursor.fetchone()
    if  result:
        return {
            "attended_hours" : result[0],
            "total_hours" : result[1],
            "attendance_percentage" : result[2]
        }
    else:
        return {"message" : "Student Not Found"}