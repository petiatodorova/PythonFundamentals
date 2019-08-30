name = input()
max_sum = 0
winner = None

while not name == 'STOP':
    current_name_sum = 0
    for letter in name:
        current_name_sum += ord(letter)

    if current_name_sum > max_sum:
        max_sum = current_name_sum
        winner = name

    name = input()

print(f'Winner is {winner} - {max_sum}!')