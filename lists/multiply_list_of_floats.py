list_floats = [float(item) for item in input().split(" ")]
number = float(input())

list_floats = [item * number for item in list_floats]

for element in list_floats:
    print(f'{element:.12g}', end=" ")
