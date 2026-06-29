from pydantic import BaseModel, EmailStr

from app.models.enums import UserRole


class UserRegister(BaseModel):
    email: EmailStr
    phone: str
    password: str
    role: UserRole


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str