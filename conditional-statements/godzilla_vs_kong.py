budget = float(input())
count_statists = int(input())
price_costume = float(input())


decor = budget * 0.10
price_costumes = 0

if count_statists > 150:
    price_costumes += count_statists * price_costume * 0.9
else:
    price_costumes += count_statists * price_costume

balance = budget - (decor + price_costumes)

if balance < 0:
    print('Not enough money!')
    print(f'Wingard needs {abs(balance):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {balance:.2f} leva left.')