from fastapi import APIRouter

from models import Department

from controlars.department_controller import Add_department,Get_all_department,Get_department_by_ID,Update_department,Delete_department



Department_Router = APIRouter(
    prefix="/Department",
    tags=["Department"]
)


@Department_Router.post("/Add")
async def add_department(department: Department):
    return await Add_department(department)


@Department_Router.get("/Get_all")
async def get_all_department():
    return await Get_all_department()


@Department_Router.get("/Get_by_ID/{department_id}")
async def get_department_by_ID(department_id: str):
    return await Get_department_by_ID(department_id)


@Department_Router.put("/Update/{department_id}")
async def update_department(
    department_id: str,
    department: Department
):
    return await Update_department(
        department_id,
        department
    )


@Department_Router.delete("/Delete/{department_id}")
async def delete_department(department_id: str):
    return await Delete_department(department_id)