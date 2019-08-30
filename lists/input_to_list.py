def input_to_list_ints():
    values = input()
    lst = values.split(' ')
    while "" in lst:
        lst.remove("")
    return [int(item) for item in lst]


if __name__ == "__main__":
    lst1 = input_to_list_ints()
    print(f'{lst1}')
