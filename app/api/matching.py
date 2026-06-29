from fastapi import APIRouter

from pydantic import BaseModel

from app.services.matching_service import MatchingService

router = APIRouter(
    prefix="/matching",
    tags=["Matching"],
)


class DriverLocation(BaseModel):
    driver_id: str
    latitude: float
    longitude: float


class RideRequest(BaseModel):
    latitude: float
    longitude: float


@router.post("/driver-location")
def update_location(data: DriverLocation):

    MatchingService.update_driver_location(
        data.driver_id,
        data.latitude,
        data.longitude,
    )

    return {
        "message": "Location Updated"
    }


@router.post("/find-driver")
def find_driver(data: RideRequest):

    driver = MatchingService.find_nearest_driver(
        data.latitude,
        data.longitude,
    )

    return {
        "driver": driver
    }