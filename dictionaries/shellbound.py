import math

town_count = {}

line = input()

while not line == "Aggregate":
    line_lst = line.split()
    town = line_lst[0]
    counter = int(line_lst[1])
    if town not in town_count.keys():
        town_count[town] = []
    if counter not in town_count[town]:
        town_count[town].append(counter)
    line = input()

for town, counter_list in town_count.items():
    str_counters = ', '.join(str(x) for x in counter_list)
    giant_shell = math.ceil(sum(counter_list) - (sum(counter_list) / (len(counter_list))))
    print(f"{town} -> {str_counters} ({giant_shell})")





