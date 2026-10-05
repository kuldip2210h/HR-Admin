from fastapi import APIRouter

from models import Notice

from controlars.notice_controller import (
    Add_notice,
    Get_all_notice,
    Get_notice_by_ID,
    Update_notice,
    Delete_notice
)


Notice_Router = APIRouter(
    prefix="/Notice",
    tags=["Notice"]
)


@Notice_Router.post("/Add")
async def add_notice(notice: Notice):
    return await Add_notice(notice)


@Notice_Router.get("/Get_all")
async def get_all_notice():
    return await Get_all_notice()


@Notice_Router.get("/Get_by_ID/{notice_id}")
async def get_notice_by_ID(notice_id: str):
    return await Get_notice_by_ID(notice_id)


@Notice_Router.put("/Update/{notice_id}")
async def update_notice(
    notice_id: str,
    notice: Notice
):
    return await Update_notice(
        notice_id,
        notice
    )


@Notice_Router.delete("/Delete/{notice_id}")
async def delete_notice(notice_id: str):
    return await Delete_notice(notice_id)