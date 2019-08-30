input_hours = int(input())
input_minutes = int(input())

all_minutes_plus_fifteen = input_hours * 60 + input_minutes + 15

minutes = all_minutes_plus_fifteen % 60
hours = all_minutes_plus_fifteen // 60

if hours % 24 == 0:
    hours = 0

print(f'{hours}:{str(minutes).zfill(2)}')