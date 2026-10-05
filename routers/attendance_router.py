from fastapi import APIRouter, HTTPException

from models import Attendance

from controlars.attendance_controller import Add_attendance, Get_all_attendance,Get_attendance_by_ID,Delete_attendance



Attendance_Router = APIRouter(
    prefix="/Attendance",
    tags=["Attendance"]
)


@Attendance_Router.post("/Add")
async def add_attendance(attendance: Attendance):
    return await Add_attendance(attendance)


@Attendance_Router.get("/Get_all")
async def get_all_attendance():
    return await Get_all_attendance()


@Attendance_Router.get("/Get_by_ID/{attendance_id}")
async def get_attendance_by_ID(attendance_id: str):
    result = await Get_attendance_by_ID(attendance_id)
    if result.get("error") == "invalid_id":
        raise HTTPException(status_code=400, detail="Invalid attendance ID")
    if result.get("MSG") == "Attendance not found":
        raise HTTPException(status_code=404, detail="Attendance not found")
    return result


@Attendance_Router.delete("/Delete/{attendance_id}")
async def delete_attendance(attendance_id: str):
    result = await Delete_attendance(attendance_id)
    if result.get("error") == "invalid_id":
        raise HTTPException(status_code=400, detail="Invalid attendance ID")
    if result.get("MSG") == "Attendance not found":
        raise HTTPException(status_code=404, detail="Attendance not found")
    return result
