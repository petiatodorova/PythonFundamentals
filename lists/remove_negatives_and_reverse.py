lst = [int(item) for item in input().split(" ")]

lst1 = []

for element in lst:
    if element >= 0:
        lst1.append(element)

lst1.reverse()
lst1 = [str(item) for item in lst1]

if len(lst1) == 0:
    print('empty')
else:
    print(" ".join(lst1))
