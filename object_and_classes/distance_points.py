class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def create_point(x, y):
    point = Point(x, y)
    return point


points = []

x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
point_1 = create_point(x_1, y_1)
point_2 = create_point(x_2, y_2)

distance = calc_distance(point_1, point_2)
print(f"{distance:.3f}")
