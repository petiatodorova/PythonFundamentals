lst = [int(item) for item in input().split()]
lst.sort()
lst = [str(item) for item in lst]
print(" <= ".join(lst))