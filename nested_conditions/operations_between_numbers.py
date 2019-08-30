n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+':
    if (n1 + n2) % 2 == 0:
        print(f'{n1} {operator} {n2} = {n1 + n2} - even')
    else:
        print(f'{n1} {operator} {n2} = {n1 + n2} - odd')

if operator == '-':
    if (n1 - n2) % 2 == 0:
        print(f'{n1} {operator} {n2} = {n1 - n2} - even')
    else:
        print(f'{n1} {operator} {n2} = {n1 - n2} - odd')

if operator == '*':
    if (n1 * n2) % 2 == 0:
        print(f'{n1} {operator} {n2} = {n1 * n2} - even')
    else:
        print(f'{n1} {operator} {n2} = {n1 * n2} - odd')

if operator == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        print(f'{n1} / {n2} = {n1/n2:.2f}')

if operator == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        print(f'{n1} % {n2} = {n1 % n2}')

