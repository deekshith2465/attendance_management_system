
import psycopg2

conn = psycopg2.connect("postgresql://attendance_db_tezb_user:iO8Xaub1Z0g98jtTkyKb1ZD9U3mxwGmi@dpg-d6rsnup4tr6s73aajk40-a.oregon-postgres.render.com/attendance_db_tezb")

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
                   percentage FROM attendance WHERE r_no = %s """,(rno,))
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
                   UPDATE attendance SET total_hours = total_hours + %s""",(data1.total,))
    conn.commit()
    return {"message" : "Total hours updated"}

class updatereal(BaseModel):
    roll_no : int
    hours : int
@app.post("/updated_attendance")
def last(data2 : updatereal):
    cursor.execute("""
                   UPDATE attendance SET attended_hours = attended_hours + %s WHERE r_no = ? """,(data2.hours,data2.roll_no))
    conn.commit()
    return {"message" : "Attendance updated"}
    
    