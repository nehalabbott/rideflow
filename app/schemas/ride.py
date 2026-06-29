from uuid import UUID

from pydantic import BaseModel

from app.models.enums import RideStatus


class RideCreate(BaseModel):
    pickup_lat: float
    pickup_lng: float
    drop_lat: float
    drop_lng: float


class RideResponse(BaseModel):
    id: UUID
    passenger_id: UUID
    driver_id: UUID | None
    pickup_lat: float
    pickup_lng: float
    drop_lat: float
    drop_lng: float
    status: RideStatus

    model_config = {
        "from_attributes": True
    }

