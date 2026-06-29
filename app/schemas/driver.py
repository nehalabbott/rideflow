from uuid import UUID

from pydantic import BaseModel

from app.models.enums import VehicleType


class DriverCreate(BaseModel):
    vehicle_type: VehicleType
    vehicle_number: str
    license_number: str


class DriverResponse(BaseModel):
    id: UUID
    user_id: UUID
    vehicle_type: VehicleType
    vehicle_number: str
    license_number: str
    is_online: bool

    model_config = {
        "from_attributes": True
    }


class DriverStatusUpdate(BaseModel):
    is_online: bool