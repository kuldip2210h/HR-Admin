from fastapi import APIRouter

from models import Leave

from controlars.leave_controller import (
    Add_leave,
    Get_all_leave,
    Get_leave_by_ID,
    Update_leave,
    Delete_leave
)


Leave_Router = APIRouter(
    prefix="/Leave",
    tags=["Leave"]
)


@Leave_Router.post("/Add")
async def add_leave(leave: Leave):
    return await Add_leave(leave)


@Leave_Router.get("/Get_all")
async def get_all_leave():
    return await Get_all_leave()


@Leave_Router.get("/Get_by_ID/{leave_id}")
async def get_leave_by_ID(leave_id: str):
    return await Get_leave_by_ID(leave_id)


@Leave_Router.put("/Update/{leave_id}")
async def update_leave(
    leave_id: str,
    leave: Leave
):
    return await Update_leave(
        leave_id,
        leave
    )


@Leave_Router.delete("/Delete/{leave_id}")
async def delete_leave(leave_id: str):
    return await Delete_leave(leave_id)