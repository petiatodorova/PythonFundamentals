x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = abs(x1 - x2)
length = abs(y1 - y2)

face = width * length
perimeter = 2 * (width + length)

print(f'{face:.2f}')
print(f'{perimeter:.2f}')
