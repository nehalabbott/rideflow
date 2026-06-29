from uuid import UUID

from sqlalchemy import Enum, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel
from app.models.enums import RideStatus


class Ride(BaseModel):

    __tablename__ = "rides"

    passenger_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    driver_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    pickup_lat: Mapped[float] = mapped_column(Float)
    pickup_lng: Mapped[float] = mapped_column(Float)

    drop_lat: Mapped[float] = mapped_column(Float)
    drop_lng: Mapped[float] = mapped_column(Float)

    status: Mapped[RideStatus] = mapped_column(
        Enum(RideStatus),
        default=RideStatus.REQUESTED,
    )