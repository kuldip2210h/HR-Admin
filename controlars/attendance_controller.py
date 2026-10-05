from db import attendance_collection
from models import Attendance
from bson import ObjectId


async def Add_attendance(attendance: Attendance):
    try:
        attendance_dict = attendance.dict()

        result = await attendance_collection.insert_one(attendance_dict)

        return {
            "MSG": "Attendance added successfully",
            "attendance_id": str(result.inserted_id)
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_all_attendance():
    try:
        attendance = []

        data = attendance_collection.find()

        async for item in data:
            item["_id"] = str(item["_id"])
            attendance.append(item)

        return attendance

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_attendance_by_ID(attendance_id: str):
    try:
        if not ObjectId.is_valid(attendance_id):
            return {"error": "invalid_id"}
        data = await attendance_collection.find_one({
            "_id": ObjectId(attendance_id)
        })

        if not data:
            return {
                "MSG": "Attendance not found"
            }

        data["_id"] = str(data["_id"])

        return data

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Delete_attendance(attendance_id: str):
    try:
        if not ObjectId.is_valid(attendance_id):
            return {"error": "invalid_id"}
        result = await attendance_collection.delete_one({
            "_id": ObjectId(attendance_id)
        })

        if result.deleted_count == 0:
            return {
                "MSG": "Attendance not found"
            }

        return {
            "MSG": "Attendance deleted successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }
