needed_money = float(input())
available_money = float(input())

total_days_count = 0
spend_days_count = 0

while True:
    if needed_money <= available_money:
        print(f'You saved the money for {total_days_count} days.')
        break

    if spend_days_count == 5:
        print(f"You can't save the money.")
        print(f'{total_days_count}')
        break

    command = input()
    current_money = float(input())
    total_days_count += 1

    if command == 'save':
        available_money += current_money
        spend_days_count = 0
    elif command == 'spend':
        spend_days_count += 1
        if current_money >= available_money:
            available_money = 0
        else:
            available_money -= current_money




