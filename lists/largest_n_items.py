lst = [int(item) for item in input().split()]
n = int(input())

lst.sort(reverse=True)
lst1 = list(lst)[0:n]
lst1 = [str(item) for item in lst1]
print(" ".join(lst1))
