from app.algorithms.quadtree import Boundary, Point, QuadTree

boundary = Boundary(
    x=30,
    y=76,
    width=2,
    height=2,
)

tree = QuadTree(boundary, capacity=2)

drivers = [
    Point(30.733, 76.779, "driver1"),
    Point(30.720, 76.800, "driver2"),
    Point(30.740, 76.760, "driver3"),
    Point(30.750, 76.770, "driver4"),
    Point(30.710, 76.810, "driver5"),
]

for driver in drivers:
    tree.insert(driver)


def print_tree(node, level=0):
    indent = "    " * level

    print(
        f"{indent}Node "
        f"(Points={len(node.points)}, Divided={node.divided})"
    )

    for point in node.points:
        print(
            f"{indent}  -> {point.driver_id}"
            f" ({point.x}, {point.y})"
        )

    if node.divided:
        print(f"{indent}NW")
        print_tree(node.northwest, level + 1)

        print(f"{indent}NE")
        print_tree(node.northeast, level + 1)

        print(f"{indent}SW")
        print_tree(node.southwest, level + 1)

        print(f"{indent}SE")
        print_tree(node.southeast, level + 1)


print_tree(tree)

search = Boundary(
    x=30.70,
    y=76.75,
    width=0.08,
    height=0.08,
)

drivers = tree.query(search)

print(drivers)