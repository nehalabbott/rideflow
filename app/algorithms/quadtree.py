from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: float
    y: float
    driver_id: str


@dataclass
class Boundary:
    x: float
    y: float
    width: float
    height: float

    def contains(self, point: Point) -> bool:
        return (
            self.x <= point.x <= self.x + self.width
            and
            self.y <= point.y <= self.y + self.height
        )

    def intersects(self, other: "Boundary") -> bool:
        return not (
            other.x > self.x + self.width
            or other.x + other.width < self.x
            or other.y > self.y + self.height
            or other.y + other.height < self.y
        )


class QuadTree:

    def __init__(self, boundary: Boundary, capacity: int = 4):
        self.boundary = boundary
        self.capacity = capacity

        self.points: List[Point] = []

        self.divided = False

        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None

    def insert(self, point: Point) -> bool:

        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity and not self.divided:
            self.points.append(point)
            return True

        if not self.divided:
            self.subdivide()

        return (
            self.northwest.insert(point)
            or self.northeast.insert(point)
            or self.southwest.insert(point)
            or self.southeast.insert(point)
        )

    def subdivide(self) -> None:

        x = self.boundary.x
        y = self.boundary.y

        w = self.boundary.width / 2
        h = self.boundary.height / 2

        self.northwest = QuadTree(
            Boundary(x, y + h, w, h),
            self.capacity,
        )

        self.northeast = QuadTree(
            Boundary(x + w, y + h, w, h),
            self.capacity,
        )

        self.southwest = QuadTree(
            Boundary(x, y, w, h),
            self.capacity,
        )

        self.southeast = QuadTree(
            Boundary(x + w, y, w, h),
            self.capacity,
        )

        self.divided = True

        old_points = self.points
        self.points = []

        for point in old_points:
            self.insert(point)

    def query(
        self,
        boundary: Boundary,
        found: List[Point] | None = None,
    ) -> List[Point]:

        if found is None:
            found = []

        if not self.boundary.intersects(boundary):
            return found

        for point in self.points:
            if boundary.contains(point):
                found.append(point)

        if self.divided:
            self.northwest.query(boundary, found)
            self.northeast.query(boundary, found)
            self.southwest.query(boundary, found)
            self.southeast.query(boundary, found)

        return found