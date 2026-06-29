from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.driver import DriverCreate, DriverResponse
from app.services.driver_service import DriverService

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"],
)


@router.post(
    "/profile",
    response_model=DriverResponse,
)
def create_driver_profile(
    driver: DriverCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return DriverService.create_profile(
            db,
            current_user,
            driver,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )