from enum import Enum


class UserRole(str, Enum):
    PASSENGER = "PASSENGER"
    DRIVER = "DRIVER"
    ADMIN = "ADMIN"
    
class VehicleType(str, Enum):
    BIKE = "BIKE"
    AUTO = "AUTO"
    CAR = "CAR"

class RideStatus(str, Enum):
    REQUESTED = "REQUESTED"
    ACCEPTED = "ACCEPTED"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"