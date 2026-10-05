import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my-secret-key-123456"
ALGORITHM = "HS256"


def create_token(data: dict):

    payload = data.copy()

    payload["exp"] = datetime.utcnow() + timedelta(hours=24)

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token: str):

    try:

        data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return data

    except:

        return None