from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from routers.auth_router import User_Router
from routers.attendance_router import Attendance_Router
from routers.department_router import Department_Router
from routers.employee_router import Employee_Router
from routers.leave_router import Leave_Router
from routers.notice_router import Notice_Router
from routers.salary_router import Salary_Router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

FRONTEND_DIR = Path(__file__).parent / "frontend"
app.mount("/assets", StaticFiles(directory=FRONTEND_DIR), name="assets")



app.include_router(User_Router)
app.include_router(Attendance_Router)
app.include_router(Department_Router)
app.include_router(Employee_Router)
app.include_router(Leave_Router)
app.include_router(Notice_Router)
app.include_router(Salary_Router)



@app.get("/")
async def home():
    return FileResponse(FRONTEND_DIR / "index.html")


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )