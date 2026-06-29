
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.models.enums import UserRole


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    phone: str
    role: UserRole
    is_verified: bool

    model_config = {
        "from_attributes": True
    }