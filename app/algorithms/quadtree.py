from dataclasses import dataclass

@dataclass
class Point:

    x: float
    y: float
    driver_id: str

class Boundary:

    def __init__(
        self,
        x,
        y,
        width,
        height,
    ):

        self.x = x
        self.y = y

        self.width = width
        self.height = height
    
    def contains(self, point):

        return (

            self.x <= point.x <= self.x + self.width

            and

            self.y <= point.y <= self.y + self.height

        )
    
class QuadTree:

    def __init__(
        self,
        boundary,
        capacity=4,
    ):

        self.boundary = boundary

        self.capacity = capacity

        self.points = []

        self.divided = False
        
    def insert(self, point):

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
    def subdivide(self):

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