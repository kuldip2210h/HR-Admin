from db import employee_collection
from models import Employee
from bson import ObjectId


async def Add_employee(employee: Employee):
    try:
        employee_dict = employee.dict()

        result = await employee_collection.insert_one(employee_dict)

        return {
            "MSG": "Employee added successfully",
            "employee_id": str(result.inserted_id)
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_all_employee():
    try:
        employees = []

        data = employee_collection.find()

        async for item in data:
            item["_id"] = str(item["_id"])
            employees.append(item)

        return employees

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_employee_by_ID(employee_id: str):
    try:
        data = await employee_collection.find_one({
            "_id": ObjectId(employee_id)
        })

        if not data:
            return {
                "MSG": "Employee not found"
            }

        data["_id"] = str(data["_id"])

        return data

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Update_employee(
    employee_id: str,
    employee: Employee
):
    try:
        result = await employee_collection.update_one(
            {"_id": ObjectId(employee_id)},
            {"$set": employee.dict()}
        )

        if result.matched_count == 0:
            return {
                "MSG": "Employee not found"
            }

        return {
            "MSG": "Employee updated successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Delete_employee(employee_id: str):
    try:
        result = await employee_collection.delete_one({
            "_id": ObjectId(employee_id)
        })

        if result.deleted_count == 0:
            return {
                "MSG": "Employee not found"
            }

        return {
            "MSG": "Employee deleted successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }