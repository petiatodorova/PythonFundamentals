numbers_list = list(map(int, input().split()))
manipulated_nums_list = list(map(lambda a: a ** 2, numbers_list))
# manipulated_nums_list = list(filter(lambda a: a % 2 == 0, numbers_list))
# manipulated_nums_list = [num for num in numbers_list if num % 2 == 0]
print(manipulated_nums_list)