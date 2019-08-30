n = int(input())
min_number = int(input())

while True:
    n -= 1
    if n <= 0:
        break

    current_number = int(input())
    if current_number < min_number:
        min_number = current_number

print(f'{min_number}')