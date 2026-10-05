from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    role: str = "employee"


class Login(BaseModel):
    username: str
    password: str


# attendence:::
class Attendance(BaseModel):
    employee_id: str
    date: str
    status: str


# deparment:::::::
class Department(BaseModel):
    name: str
    description: str


# employeee::::
class Employee(BaseModel):
    name: str
    email: str
    phone: str
    department_id: str
    position: str
    salary: float
    joining_date: str


# leaves::::::::
class Leave(BaseModel):
    employee_id: str
    leave_type: str
    start_date: str
    end_date: str
    reason: str
    status: str


# notice:::::::::::
class Notice(BaseModel):
    title: str
    description: str
    date: str
    created_by: str    


# salary :::::::::::
class Salary(BaseModel):
    employee_id: str
    basic_salary: float
    allowance: float
    deduction: float
    month: str
    year: int
    status: str