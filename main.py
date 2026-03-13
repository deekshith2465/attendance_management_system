
import sqlite3

conn = sqlite3.connect("Attendance.db", check_same_thread=False)

cursor = conn.cursor()
from fastapi.responses import FileResponse
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory=".")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/admin.html")
def admin_page():
    return FileResponse("admin.html")
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

class Login(BaseModel):
    password : int
    
@app.post("/auth")
def check_auth(data : Login):
    Main_Pass = 24052006
    if data.password == Main_Pass:
        return {"message" : "login successful"}
    else:
        return {"message" : "Invalid Password"}


#update total hours
class Update(BaseModel):
    total : int
@app.post("/update_total")
def update_total(data1 : Update):
    cursor.execute("""
                   UPDATE attendance SET total_hours = total_hours + ?""",(data1.total,))
    conn.commit()
    return {"message" : "Total hours updated"}

class updatereal(BaseModel):
    roll_no : int
    hours : int
@app.post("/updated_attendance")
def last(data2 : updatereal):
    cursor.execute("""
                   UPDATE attendance SET attended_hours = attended_hours + ? WHERE r_no = ? """,(data2.hours,data2.roll))
    conn.commit()
    return {"message" : "Attendance updated"}
    
    