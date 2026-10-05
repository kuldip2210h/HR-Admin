from fastapi import APIRouter

from models import Employee

from controlars.employee_controller import (
    Add_employee,
    Get_all_employee,
    Get_employee_by_ID,
    Update_employee,
    Delete_employee
)


Employee_Router = APIRouter(
    prefix="/Employee",
    tags=["Employee"]
)


@Employee_Router.post("/Add")
async def add_employee(employee: Employee):
    return await Add_employee(employee)


@Employee_Router.get("/Get_all")
async def get_all_employee():
    return await Get_all_employee()


@Employee_Router.get("/Get_by_ID/{employee_id}")
async def get_employee_by_ID(employee_id: str):
    return await Get_employee_by_ID(employee_id)


@Employee_Router.put("/Update/{employee_id}")
async def update_employee(
    employee_id: str,
    employee: Employee
):
    return await Update_employee(
        employee_id,
        employee
    )


@Employee_Router.delete("/Delete/{employee_id}")
async def delete_employee(employee_id: str):
    return await Delete_employee(employee_id)