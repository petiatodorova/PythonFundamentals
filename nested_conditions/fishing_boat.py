budget = int(input())
season = input()
count_fishermans = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if count_fishermans <= 6:
    price = price * 0.90
elif 7 < count_fishermans <= 11:
    price = price * 0.85
elif count_fishermans >= 12:
    price = price * 0.75

if (count_fishermans % 2 == 0) and not (season == 'Autumn'):
    price = price * 0.95

if budget >= price:
    print(f'Yes! You have {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(price - budget):.2f} leva.')
