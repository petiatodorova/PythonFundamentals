lst = [int(item) for item in input().split()]
lst_unique_numbers = list(set(lst))
lst_unique_numbers.sort()


for number in lst_unique_numbers:
    print(f'{number} -> {lst.count(number)}')
