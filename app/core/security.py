import bcrypt
from datetime import datetime, timedelta, UTC

from jose import jwt, JWTError

from app.core.config import settings


ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )


def create_access_token(data: dict) -> str:
    payload = data.copy()

    payload["exp"] = (
        datetime.now(UTC)
        + timedelta(minutes=60)
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )
def decode_access_token(token: str) -> dict:
    print("TOKEN RECEIVED:", token)

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        print("PAYLOAD:", payload)
        return payload

    except Exception as e:
        print("JWT ERROR:", repr(e))
        raise ValueError("Invalid token")