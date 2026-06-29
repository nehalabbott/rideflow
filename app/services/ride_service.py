from app.models.enums import UserRole
from app.models.user import User
from app.schemas.ride import RideCreate

from app.services.matching_service import MatchingService


class RideService:

    @staticmethod
    def request_ride(
        current_user: User,
        ride: RideCreate,
    ):

        if current_user.role != UserRole.PASSENGER:
            raise ValueError(
                "Only passengers can request rides."
            )

        driver = MatchingService.find_nearest_driver(
            ride.pickup_lat,
            ride.pickup_lng,
        )

        if driver is None:
            return {
                "message": "No drivers available"
            }

        return {
            "message": "Driver Assigned",
            "driver": driver,
            "pickup": {
                "lat": ride.pickup_lat,
                "lng": ride.pickup_lng,
            },
            "drop": {
                "lat": ride.drop_lat,
                "lng": ride.drop_lng,
            }
        }