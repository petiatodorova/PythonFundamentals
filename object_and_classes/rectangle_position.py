class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.right = width + left
        self.bottom = top + height


rectangles = []

for n in range(2):
    line = list(map(int, input().split()))
    cur_left = line[0]
    cur_top = line[1]
    cur_width = line[2]
    cur_height = line[3]
    current_rect = Rectangle(cur_left, cur_top, cur_width, cur_height)
    rectangles.append(current_rect)

if rectangles[0].left >= rectangles[1].left \
        and rectangles[0].top <= rectangles[1].top \
        and rectangles[0].right <= rectangles[1].right \
        and rectangles[0].bottom <= rectangles[1].bottom:
    print("Inside")
else:
    print("Not inside")

