def print_dashes(n):
    for counter in range(1, 2 * n + 1):
        print('-', end="")
    print()


def print_one_row(n):
    print('-', end="")
    for counter in range(1, n):
        print('\\/', end="")
    print('-')


def print_rows(n):
    for row in range(1, n - 1):
        print_one_row(n)


def print_figure(n):
    print_dashes(n)
    print_rows(n)
    print_dashes(n)


if __name__ == "__main__":
    number = int(input())
    print_figure(number)
