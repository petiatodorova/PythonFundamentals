player_name = input()
goals_count = None
best_player = None
max_goals = 0

while True:
    if player_name == "END":
        break

    goals_count = int(input())
    if goals_count >= 10:
        max_goals = goals_count
        best_player = player_name
        break

    if goals_count > max_goals:
        max_goals = goals_count
        best_player = player_name

    player_name = input()

print(f'{best_player} is the best player!')
if max_goals >= 3:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')
