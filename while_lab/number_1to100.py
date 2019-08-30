number = int(input())

while not (1 <= number <= 100):
    print('Invalid number!')
    number = int(input())

print(f'The number is: {number}')