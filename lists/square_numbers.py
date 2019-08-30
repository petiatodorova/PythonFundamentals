import math

lst = list(map(int, input().split()))
lst_squares = [num for num in lst if num >= 0]
lst_squares = [num for num in lst_squares if math.sqrt(num) == int(math.sqrt(num))]
lst_squares.sort(reverse=True)

print(*lst_squares)