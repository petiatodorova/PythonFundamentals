lst = input().split('|')
lst.reverse()
lst1 = []

for element in lst:
    lst1 += element.split()

print(" ".join(lst1))
