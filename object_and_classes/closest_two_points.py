import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MinDistance:
    def __init__(self, point_one_x, point_one_y, point_two_x, point_two_y, dist):
        self.p1_x = point_one_x
        self.p1_y = point_one_y
        self.p2_x = point_two_x
        self.p2_y = point_two_y
        self.dist = dist


def distance(point_1, point_2):
    return ((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2) ** 0.5


all_points = []
all_min_pairs = []

n = int(input())

for num in range(n):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    point = Point(x, y)
    all_points.append(point)

for point in all_points:
    min_dist = sys.float_info.max
    for point_other in all_points:
        if point_other is not point:
            min_pair = MinDistance(point.x, point.y, point_other.x, point_other.y, min_dist)
            if distance(point, point_other) < min_dist:
                min_dist = distance(point, point_other)
                min_pair = MinDistance(point.x, point.y, point_other.x, point_other.y, min_dist)
            all_min_pairs.append(min_pair)

sorted_min_pair = sorted(all_min_pairs, key=lambda pair: pair.dist)
the_pair = sorted_min_pair[0]

print(f"{the_pair.dist:.3f}")
print(f"({the_pair.p1_x}, {the_pair.p1_y})")
print(f"({the_pair.p2_x}, {the_pair.p2_y})")
