import math

lst = [float(item) for item in input().split()]
lst_square = []

for number in lst:
    if math.ceil(math.sqrt(number)) == math.floor(math.sqrt(number)):
        lst_square.append(number)

lst_square.sort(reverse=True)

lst_square = [str(itemA) for itemA in lst_square]

print(" ".join(lst_square))