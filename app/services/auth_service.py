from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.schemas.auth import UserRegister


class AuthService:

    @staticmethod
    def register(db: Session, user: UserRegister) -> User:

        existing = db.query(User).filter(
            User.email == user.email
        ).first()

        if existing:
            raise ValueError("Email already registered")

        new_user = User(
            email=user.email,
            phone=user.phone,
            password_hash=hash_password(user.password),
            role=user.role,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    @staticmethod
    def login(
            db: Session,
            email: str,
            password: str,
        ) -> str:

            # Find user by email
        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user:
            raise ValueError("Invalid email or password")

        # Verify password
        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

            # Generate JWT
        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return access_token