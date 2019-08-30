budget = int(input())
n = int(input())
total_sum = 0

for counter in range(n):
    article = input()
    if article == 'hoodie':
        total_sum += 30
    elif article == 'keychain':
        total_sum += 4
    elif article == 'T-shirt':
        total_sum += 20
    elif article == 'flag':
        total_sum += 15
    elif article == 'sticker':
        total_sum += 1

if budget >= total_sum:
    print(f'You bought {n} items and left with {budget - total_sum} lv.')
else:
    print(f'Not enough money, you need {total_sum - budget} more lv.')