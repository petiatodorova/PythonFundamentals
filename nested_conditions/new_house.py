type_flower = input()
count_flowers = int(input())
budget = int(input())

total_sum = 0

ROSES_PRICE = 5.00
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3.00
GLADIOLUS_PRICE = 2.50

if type_flower == 'Roses':
    if count_flowers <= 80:
        total_sum = count_flowers * ROSES_PRICE
    else:
        total_sum = count_flowers * ROSES_PRICE * 0.90

elif type_flower == 'Dahlias':
    if count_flowers <= 90:
        total_sum = count_flowers * DAHLIAS_PRICE
    else:
        total_sum = count_flowers * DAHLIAS_PRICE * 0.85

elif type_flower == 'Tulips':
    if count_flowers <= 80:
        total_sum = count_flowers * TULIPS_PRICE
    else:
        total_sum = count_flowers * TULIPS_PRICE * 0.85

elif type_flower == 'Narcissus':
    if count_flowers < 120:
        total_sum = count_flowers * NARCISSUS_PRICE * 1.15
    else:
        total_sum = count_flowers * NARCISSUS_PRICE

elif type_flower == 'Gladiolus':
    if count_flowers < 80:
        total_sum = count_flowers * GLADIOLUS_PRICE * 1.20
    else:
        total_sum = count_flowers * GLADIOLUS_PRICE

if budget >= total_sum:
    print(f'Hey, you have a great garden with {count_flowers} {type_flower} and {(budget - total_sum):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_sum - budget):.2f} leva more.')
