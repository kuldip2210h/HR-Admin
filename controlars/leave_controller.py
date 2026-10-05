from db import leave_collection
from models import Leave
from bson import ObjectId


async def Add_leave(leave: Leave):
    try:
        leave_dict = leave.dict()

        result = await leave_collection.insert_one(leave_dict)

        return {
            "MSG": "Leave added successfully",
            "leave_id": str(result.inserted_id)
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_all_leave():
    try:
        leaves = []

        data = leave_collection.find()

        async for item in data:
            item["_id"] = str(item["_id"])
            leaves.append(item)

        return leaves

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_leave_by_ID(leave_id: str):
    try:
        data = await leave_collection.find_one({
            "_id": ObjectId(leave_id)
        })

        if not data:
            return {
                "MSG": "Leave not found"
            }

        data["_id"] = str(data["_id"])

        return data

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Update_leave(
    leave_id: str,
    leave: Leave
):
    try:
        result = await leave_collection.update_one(
            {"_id": ObjectId(leave_id)},
            {"$set": leave.dict()}
        )

        if result.matched_count == 0:
            return {
                "MSG": "Leave not found"
            }

        return {
            "MSG": "Leave updated successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Delete_leave(leave_id: str):
    try:
        result = await leave_collection.delete_one({
            "_id": ObjectId(leave_id)
        })

        if result.deleted_count == 0:
            return {
                "MSG": "Leave not found"
            }

        return {
            "MSG": "Leave deleted successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }