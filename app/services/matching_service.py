from math import sqrt

from app.algorithms.quadtree import Boundary
from app.algorithms.quadtree import Point
from app.algorithms.quadtree import QuadTree

SEARCH_RADIUS = 0.05

drivers = {}

boundary = Boundary(
    x=30,
    y=76,
    width=2,
    height=2,
)

tree = QuadTree(boundary)


class MatchingService:

    @staticmethod
    def update_driver_location(driver_id, lat, lng):

        drivers[driver_id] = {
            "lat": lat,
            "lng": lng,
        }

        MatchingService.rebuild_tree()

    @staticmethod
    def find_nearest_driver(lat, lng):

        # First search a nearby region using QuadTree
        search = Boundary(
            x=lat - SEARCH_RADIUS,
            y=lng - SEARCH_RADIUS,
            width=2 * SEARCH_RADIUS,
            height=2 * SEARCH_RADIUS,
        )

        nearby = tree.query(search)

        best_driver = None
        best_distance = float("inf")

        # Fast path: search nearby drivers
        if nearby:

            for point in nearby:

                distance = sqrt(
                    (point.x - lat) ** 2
                    + (point.y - lng) ** 2
                )

                if distance < best_distance:
                    best_distance = distance
                    best_driver = point

        # Fallback: search all drivers if nearby search is empty
        else:

            for driver_id, location in drivers.items():

                distance = sqrt(
                    (location["lat"] - lat) ** 2
                    + (location["lng"] - lng) ** 2
                )

                if distance < best_distance:
                    best_distance = distance
                    best_driver = Point(
                        x=location["lat"],
                        y=location["lng"],
                        driver_id=driver_id,
                    )

        if best_driver is None:
            return None

        return {
            "driver_id": best_driver.driver_id,
            "distance": round(best_distance, 5),
        }
    
    @staticmethod
    def rebuild_tree():

        global tree

        tree = QuadTree(boundary)

        for driver_id, location in drivers.items():

            tree.insert(
                Point(
                    x=location["lat"],
                    y=location["lng"],
                    driver_id=driver_id,
                )
            )