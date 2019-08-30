n = int(input())
max_number = int(input())

while True:
    if n <= 1:
        break

    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    n -= 1

print(f'{max_number}')