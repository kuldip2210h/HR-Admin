from fastapi import APIRouter

from models import Salary

from controlars.salary_controller import (
    Add_salary,
    Get_all_salary,
    Get_salary_by_ID,
    Update_salary,
    Delete_salary
)


Salary_Router = APIRouter(
    prefix="/Salary",
    tags=["Salary"]
)


@Salary_Router.post("/Add")
async def add_salary(salary: Salary):
    return await Add_salary(salary)


@Salary_Router.get("/Get_all")
async def get_all_salary():
    return await Get_all_salary()


@Salary_Router.get("/Get_by_ID/{salary_id}")
async def get_salary_by_ID(salary_id: str):
    return await Get_salary_by_ID(salary_id)


@Salary_Router.put("/Update/{salary_id}")
async def update_salary(
    salary_id: str,
    salary: Salary
):
    return await Update_salary(
        salary_id,
        salary
    )


@Salary_Router.delete("/Delete/{salary_id}")
async def delete_salary(salary_id: str):
    return await Delete_salary(salary_id)