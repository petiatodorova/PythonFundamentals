import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_info(self):
        return f"{self.x}:{self.y}"

    @staticmethod
    def calc_distance(point_1, point_2):
       return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)


class Box:
    def __init__(self, upper_left: Point, upper_right: Point, bottom_left: Point, bottom_right: Point):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.height = self.calc_height()
        self.width = self.calc_width()

    def calc_width(self):
        return Point.calc_distance(self.upper_left, self.upper_right)

    def calc_height(self):
        return Point.calc_distance(self.upper_left, self.bottom_left)

    def calc_perimeter(self):
        return self.height * 2 + self.width * 2

    def calc_area(self):
        return self.width * self.height

    def box_show_info(self):
        return f"Box: {self.width:.0f}, {self.height:.0f}\nPerimeter: {self.calc_perimeter():.0f}\nArea: {self.calc_area():.0f}"


def create_point(coordinates):
    x, y = [int(num) for num in coordinates.split(":")]
    point = Point(x, y)
    return point


def create_box(up_left, up_right, bot_left, bot_right):
    upper_left = create_point(up_left)
    upper_right = create_point(up_right)
    bottom_left = create_point(bot_left)
    bottom_right = create_point(bot_right)
    return Box(upper_left, upper_right, bottom_left, bottom_right)


input_line = input().split(" | ")

while not input_line[0] == "end":
    box = create_box(input_line[0], input_line[1], input_line[2], input_line[3])
    print(box.box_show_info())
    input_line = input().split(" | ")