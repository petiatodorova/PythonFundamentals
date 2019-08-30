product = input()
town = input()
quantity = float(input())

sum = 0

if product == 'coffee':
    if town == 'Sofia':
        sum += 0.50 * quantity
    elif town == 'Plovdiv':
        sum += 0.40 * quantity
    elif town == 'Varna':
        sum += 0.45 * quantity

elif product == 'water':
    if town == 'Sofia':
        sum += 0.80 * quantity
    elif town == 'Plovdiv':
        sum += 0.70 * quantity
    elif town == 'Varna':
        sum += 0.70 * quantity

elif product == 'beer':
    if town == 'Sofia':
        sum += 1.20 * quantity
    elif town == 'Plovdiv':
        sum += 1.15 * quantity
    elif town == 'Varna':
        sum += 1.10 * quantity

elif product == 'sweets':
    if town == 'Sofia':
        sum += 1.45 * quantity
    elif town == 'Plovdiv':
        sum += 1.30 * quantity
    elif town == 'Varna':
        sum += 1.35 * quantity

elif product == 'peanuts':
    if town == 'Sofia':
        sum += 1.60 * quantity
    elif town == 'Plovdiv':
        sum += 1.50 * quantity
    elif town == 'Varna':
        sum += 1.55 * quantity

print(sum)