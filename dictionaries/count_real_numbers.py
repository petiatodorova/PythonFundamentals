numbers = list(map(float, input().split()))

dict_counter = {}

for num in numbers:
    if num in dict_counter:
        dict_counter[num] += 1
    else:
        dict_counter[num] = 1

for item in sorted(dict_counter.keys()):
    print(f"{item} -> {dict_counter[item]} times")