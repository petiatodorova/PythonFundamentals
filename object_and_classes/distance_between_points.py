class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


points = []

for num in range(2):
    line = input().split()
    x = float(line[0])
    y = float(line[1])
    point = Point(x, y)
    points.append(point)

the_distance = distance(points[0], points[1])
print(f"{the_distance:.3f}")
