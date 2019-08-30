steps_count = 0
command = input()

while True:
    if command == 'Going home':
        steps_count += int(input())
        if steps_count >= 10000:
            print(f'Goal reached! Good job!')
        else:
            print(f'{10000 - steps_count} more steps to reach goal.')
        break

    steps_count += int(command)

    if steps_count >= 10000:
        print(f'Goal reached! Good job!')
        break

    command = input()


