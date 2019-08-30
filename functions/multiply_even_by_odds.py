def sum_even_digits(num):
    even_digits_sum = 0
    for char in num:
        if char == '-':
            continue
        digit = int(char)
        if digit % 2 == 0:
            even_digits_sum += digit
    return even_digits_sum


def sum_odd_digits(num):
    odd_digits_sum = 0
    for char in num:
        if char == '-':
            continue
        digit = int(char)
        if digit % 2 != 0:
            odd_digits_sum += digit
    return odd_digits_sum


if __name__ == "__main__":
    number = input()
    result = sum_even_digits(number) * sum_odd_digits(number)
    print(result)