lst = [float(item) for item in input().split()]

index = 0

while index < len(lst) - 1:
    if lst[index] != lst[index + 1]:
        index += 1
    else:
        lst[index] = lst[index] * 2
        lst.remove(lst[index + 1])
        index -= 1
        if index == -1:
            index = 0

for num in lst:
    print(num, end=" ")
