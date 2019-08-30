command = input()
needed_sum = 0
total_saved_sum = 0
destination_name = None

while not command == 'End':
    destination_name = command
    needed_sum = float(input())
    while total_saved_sum < needed_sum:
        total_saved_sum += float(input())

    print(f'Going to {destination_name}!')
    total_saved_sum = 0
    command = input()
