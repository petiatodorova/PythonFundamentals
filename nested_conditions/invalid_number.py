number = int(input())

valid_number = (100 <= number and number <= 200) or number == 0

if not valid_number:
    print('invalid')