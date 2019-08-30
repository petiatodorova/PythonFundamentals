import math
type = input()

if type == 'square':
    side = float(input())
    face = side ** 2
elif type == 'rectangle':
    width = float(input())
    length = float(input())
    face = width * length
elif type == 'circle':
    radius = float(input())
    face = math.pi * radius ** 2
elif type == 'triangle':
    length = float(input())
    height = float(input())
    face = length * height / 2

print(f'{face:.3f}')
