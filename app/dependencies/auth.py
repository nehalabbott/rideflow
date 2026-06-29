from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    token = credentials.credentials
    print("TOKEN:", token)
    try:
        payload = decode_access_token(token)

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found",
            )

        return user

    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )