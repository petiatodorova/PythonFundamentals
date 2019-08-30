def num_pow(n, p):
    return pow(n, p)


if __name__ == "__main__":
    number = float(input())
    power = int(input())
    result = num_pow(number, power)
    print(result)