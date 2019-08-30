class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other):
        return int((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.width = self.upper_left.calculate_distance(self.upper_right)
        self.height = self.upper_left.calculate_distance(self.bottom_left)

    def calculate_perimeter(self):
        return int(2 * self.width + 2 * self.height)

    def calculate_area(self):
        return int(self.width * self.height)


boxes_list = []

input_line = input()

while not input_line == "end":
    line = list(map(int, input_line.replace(" | ", ":").split(":")))
    upper_left_point = Point(line[0], line[1])
    upper_right_point = Point(line[2], line[3])
    bottom_left_point = Point(line[4], line[5])
    bottom_right_point = Point(line[6], line[7])
    cur_box = Box(upper_left_point, upper_right_point, bottom_left_point, bottom_right_point)
    boxes_list.append(cur_box)
    input_line = input()

for box in boxes_list:
    print(f"Box: {int(box.width)}, {int(box.height)}")
    print(f"Perimeter: {box.calculate_perimeter()}")
    print(f"Area: {box.calculate_area()}")
