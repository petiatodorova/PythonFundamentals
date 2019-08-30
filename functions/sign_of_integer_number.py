def num_sign(num):
    if num < 0:
        return f'The number {num} is negative.'
    elif num == 0:
        return f'The number {num} is zero.'
    else:
        return f'The number {num} is positive.'


if __name__ == "__main__":
    number = int(input())
    result = num_sign(number)
    print(result)