from db import notice_collection
from models import Notice
from bson import ObjectId


async def Add_notice(notice: Notice):
    try:
        notice_dict = notice.dict()

        result = await notice_collection.insert_one(notice_dict)

        return {
            "MSG": "Notice added successfully",
            "notice_id": str(result.inserted_id)
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_all_notice():
    try:
        notices = []

        data = notice_collection.find()

        async for item in data:
            item["_id"] = str(item["_id"])
            notices.append(item)

        return notices

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Get_notice_by_ID(notice_id: str):
    try:
        data = await notice_collection.find_one({
            "_id": ObjectId(notice_id)
        })

        if not data:
            return {
                "MSG": "Notice not found"
            }

        data["_id"] = str(data["_id"])

        return data

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Update_notice(
    notice_id: str,
    notice: Notice
):
    try:
        result = await notice_collection.update_one(
            {"_id": ObjectId(notice_id)},
            {"$set": notice.dict()}
        )

        if result.matched_count == 0:
            return {
                "MSG": "Notice not found"
            }

        return {
            "MSG": "Notice updated successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }


async def Delete_notice(notice_id: str):
    try:
        result = await notice_collection.delete_one({
            "_id": ObjectId(notice_id)
        })

        if result.deleted_count == 0:
            return {
                "MSG": "Notice not found"
            }

        return {
            "MSG": "Notice deleted successfully"
        }

    except Exception as e:
        return {
            "MSG": str(e)
        }