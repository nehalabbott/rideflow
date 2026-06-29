from sqlalchemy import Boolean, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base import BaseModel
from app.models.enums import VehicleType
from sqlalchemy import Enum

from app.models.user import User


class Driver(BaseModel):

    __tablename__ = "driver_profiles"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    vehicle_type: Mapped[VehicleType] = mapped_column(
        Enum(VehicleType),
        nullable=False,
    )

    vehicle_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    license_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    is_online: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="driver",
    )