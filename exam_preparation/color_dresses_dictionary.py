n = int(input())

color_dress = {}

for number in range(n):
    line = input().split(' -> ')
    color = line[0]
    dresses = line[1].split(',')

    if color not in color_dress.keys():
        color_dress[color] = []
    color_dress[color].extend(dresses)

items_count_dict = {}

for color, dress_list in color_dress.items():
    items_count_dict[color] = {color: dress_list.count(color) for color in dress_list}

line = input().split()

find_color = line[0]
find_dress = line[1]
for color, dress_counter in items_count_dict.items():
    print(f"{color} clothes:")
    for dress, counter in dress_counter.items():
        if color == find_color and dress == find_dress:
            print(f"* {dress} - {counter} (found!)")
        else:
            print(f"* {dress} - {counter}")