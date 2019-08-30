lst = [int(item) for item in input().split(" ")]
counter_odd_numbers = 0

for index in range(1, len(lst), 2):
    if lst[index] % 2 != 0:
        print(f'Index {index} -> {lst[index]}')