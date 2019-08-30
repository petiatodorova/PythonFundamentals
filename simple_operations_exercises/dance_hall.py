l = float(input())
w = float(input())
a = float(input())

hall_area = l * w
wardrobe_area = a**2
bench_area = hall_area / 10
free_area = hall_area - wardrobe_area - bench_area

one_dancer_area = 7040 / 10000

count_dancers = free_area // one_dancer_area

print(int(count_dancers))