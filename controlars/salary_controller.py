from db import salary_collection
from models import Salary
from bson import ObjectId


async def Add_salary(salary: Salary):
    try:
        salary_dict = salary.dict()

        result = await salary_collection.insert_one(salary_dict)

        return {
            "MSG": "Salary added successfully",
            "salary_id": str(result.inserted_id)
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_all_salary():
    try:
        salaries = []

        data = salary_collection.find()

        async for item in data:
            item["_id"] = str(item["_id"])
            salaries.append(item)

        return salaries

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_salary_by_ID(salary_id: str):
    try:
        data = await salary_collection.find_one({
            "_id": ObjectId(salary_id)
        })

        if not data:
            return {
                "MSG": "Salary not found"
            }

        data["_id"] = str(data["_id"])

        return data

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Update_salary(
    salary_id: str,
    salary: Salary
):
    try:
        result = await salary_collection.update_one(
            {"_id": ObjectId(salary_id)},
            {"$set": salary.dict()}
        )

        if result.matched_count == 0:
            return {
                "MSG": "Salary not found"
            }

        return {
            "MSG": "Salary updated successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Delete_salary(salary_id: str):
    try:
        result = await salary_collection.delete_one({
            "_id": ObjectId(salary_id)
        })

        if result.deleted_count == 0:
            return {
                "MSG": "Salary not found"
            }

        return {
            "MSG": "Salary deleted successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }