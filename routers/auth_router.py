from fastapi import APIRouter
from models import User, Login
from utils import Register_user, Login_user

User_Router = APIRouter(
    prefix="/User",
    tags=["User"]
)


@User_Router.post("/register")
async def Register(data: User):

    return await Register_user(data)


@User_Router.post("/login")
async def Login(data: Login):

    return await Login_user(data)
