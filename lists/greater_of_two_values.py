def greater_number(one, two):
    if int(one) > int(two):
        return one
    else:
        return two


def greater_text(one, two):
    if one > two:
        return one
    else:
        return two


if __name__ == "__main__":
    kind = input()
    a = input()
    b = input()
    if kind == "char" or kind == "string":
        print(greater_text(a, b))
    else:
        print(greater_number(a, b))
