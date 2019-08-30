count_deposits = int(input())
total = 0

while True:
    current_deposit = float(input())

    if current_deposit < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {current_deposit:.2f}')
    total += current_deposit
    count_deposits -= 1
    if count_deposits == 0:
        break

print(f'Total: {total:.2f}')



