the_key = input()
the_value = input()
n = int(input())

key_values = {}

for num in range(n):
    line = input().split(" => ")
    current_key = line[0]
    current_value = line[1].split(';')
    key_values[current_key] = current_value

new_key_value = {}

for key, value in key_values.items():
    if the_key in key:
        new_key_value[key] = []
        for item in value:
            if item.__contains__(the_value):
                new_key_value[key].append(item)

for key, value in new_key_value.items():
    print(f"{key}:")
    for item in value:
        print(f"-{item}")