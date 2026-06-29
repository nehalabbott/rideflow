from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.ride import RideCreate
from app.services.ride_service import RideService

router = APIRouter(
    prefix="/rides",
    tags=["Rides"],
)


@router.post("/request")
def request_ride(
    ride: RideCreate,
    current_user: User = Depends(get_current_user),
):
    try:
        return RideService.request_ride(
            current_user,
            ride,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )