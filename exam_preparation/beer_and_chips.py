import math

BEER_PRICE = 1.20
name = input()
budget = float(input())
bottles_count = int(input())
snaks_count = int(input())

money_for_beers = bottles_count * BEER_PRICE
money_for_chips = math.ceil(snaks_count * money_for_beers * 0.45)

money_needed = money_for_beers + money_for_chips

if budget >= money_needed:
    print(f'{name} bought a snack and has {(budget - money_needed):.2f} leva left.')
else:
    print(f'{name} needs {(money_needed - budget):.2f} more leva!')
