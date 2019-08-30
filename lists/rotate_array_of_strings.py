lst = input().split(" ")
list_length = len(lst)
lst1 = lst[list_length - 1:] + lst[0:list_length - 1]
print(f'{" ".join(lst1)}')