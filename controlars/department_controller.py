from db import department_collection
from models import Department
from bson import ObjectId


async def Add_department(department: Department):
    try:
        department_dict = department.dict()

        result = await department_collection.insert_one(department_dict)

        return {
            "MSG": "Department added successfully",
            "department_id": str(result.inserted_id)
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_all_department():
    try:
        departments = []

        data = department_collection.find()

        async for item in data:
            item["_id"] = str(item["_id"])
            departments.append(item)

        return departments

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_department_by_ID(department_id: str):
    try:
        data = await department_collection.find_one({
            "_id": ObjectId(department_id)
        })

        if not data:
            return {
                "MSG": "Department not found"
            }

        data["_id"] = str(data["_id"])

        return data

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Update_department(department_id: str, department: Department):
    try:
        result = await department_collection.update_one(
            {"_id": ObjectId(department_id)},
            {"$set": department.dict()}
        )

        if result.matched_count == 0:
            return {
                "MSG": "Department not found"
            }

        return {
            "MSG": "Department updated successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Delete_department(department_id: str):
    try:
        result = await department_collection.delete_one({
            "_id": ObjectId(department_id)
        })

        if result.deleted_count == 0:
            return {
                "MSG": "Department not found"
            }

        return {
            "MSG": "Department deleted successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }