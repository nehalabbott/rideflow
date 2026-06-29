from sqlalchemy.orm import Session

from app.models.driver import Driver
from app.models.user import User
from app.schemas.driver import DriverCreate


class DriverService:

    @staticmethod
    def create_profile(
        db: Session,
        current_user: User,
        driver: DriverCreate,
    ) -> Driver:

        if current_user.role != "DRIVER":
            raise ValueError(
                "Only drivers can create driver profiles."
            )

        existing = db.query(Driver).filter(
            Driver.user_id == current_user.id
        ).first()

        if existing:
            raise ValueError(
                "Driver profile already exists."
            )

        profile = Driver(
            user_id=current_user.id,
            vehicle_type=driver.vehicle_type,
            vehicle_number=driver.vehicle_number,
            license_number=driver.license_number,
        )

        db.add(profile)
        db.commit()
        db.refresh(profile)

        return profile