def compare(first_arg, second_arg):
    if first_arg > second_arg:
        return first_arg
    else:
        return second_arg


def cast_arguments(console_line):
    if console_line == "int":
        arg_one = int(input())
        arg_two = int(input())
        return arg_one, arg_two
    elif console_line == "char" or console_line == "string":
        arg_one = input()
        arg_two = input()
        return arg_one, arg_two


def print_result():
    arguments = cast_arguments(line)
    result = compare(arguments[0], arguments[1])
    print(f"{result}")


if __name__ == "__main__":
    line = input()
    print_result()
