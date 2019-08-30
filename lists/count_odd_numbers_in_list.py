lst = [int(item) for item in input().split(" ")]
counter_odd_numbers = 0

for num in lst:
    if num % 2 != 0:
        counter_odd_numbers += 1

print(counter_odd_numbers)