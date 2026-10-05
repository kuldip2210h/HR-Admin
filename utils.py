from db import user_collection
from models import User, Login
from controlars.auth_controller import create_token


async def Register_user(data: User):

    try:

        existing_user = await user_collection.find_one(
            {
                "username": data.username
            }
        )

        if existing_user:

            return {
                "MSG": "User already exists"
            }

        result = await user_collection.insert_one(data.dict())

        return {
            "MSG": "Registration successful",
            "user_id": str(result.inserted_id)
        }

    except Exception as e:

        return {
            "MSG": "Registration failed",
            "error": str(e)
        }


async def Login_user(data: Login):

    try:

        user = await user_collection.find_one(
            {
                "username": data.username,
                "password": data.password
            }
        )

        if not user:

            return {
                "MSG": "Invalid username or password"
            }

        token = create_token(
            {
                "user_id": str(user["_id"]),
                "username": user["username"],
                "role": user["role"]
            }
        )

        return {
            "MSG": "Login successful",
            "Token": token,
            "user_id": str(user["_id"]),
            "role": user["role"]
        }

    except Exception as e:

        return {
            "MSG": "Login failed",
            "error": str(e)
        }
