def top(num):
    for row in range(1, num + 1):
        for column in range(1, row + 1):
            if column == row:
                print(f"{column}", end='\n')
            else:
                print(f"{column}", end=' ')


def bottom(num):
    for row in range(1, num):
        for column in range(1, num - row + 1):
            if column == num - row:
                print(f"{column}", end='\n')
            else:
                print(f"{column}", end=' ')


def print_triangle(num):
    top(num)
    bottom(num)


if __name__ == "__main__":
    number = int(input())
    print_triangle(number)