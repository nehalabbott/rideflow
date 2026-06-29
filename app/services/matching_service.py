from math import sqrt

drivers = {}


class MatchingService:

    @staticmethod
    def update_driver_location(driver_id, lat, lng):
        drivers[driver_id] = {
            "lat": lat,
            "lng": lng,
        }
        print("Drivers:", drivers)

    @staticmethod
    def find_nearest_driver(lat, lng):

        print("Current drivers:", drivers)

        if not drivers:
            return None

        best_driver = None
        best_distance = float("inf")

        for driver_id, location in drivers.items():

            distance = sqrt(
                (lat - location["lat"]) ** 2
                + (lng - location["lng"]) ** 2
            )

            print(driver_id, distance)

            if distance < best_distance:
                best_distance = distance
                best_driver = driver_id

        print("Chosen:", best_driver)

        return best_driver