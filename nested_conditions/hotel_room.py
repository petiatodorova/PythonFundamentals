month = input()
count_nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    if count_nights <= 7:
        studio_price = 50
    elif 7 < count_nights < 14:
        studio_price = 50 * 0.95
    elif count_nights > 14:
        studio_price = 50 * 0.7
    apartment_price = 65

elif month == 'June' or month == 'September':
    if count_nights > 14:
        studio_price = 75.20 * 0.8
    else:
        studio_price = 75.20
    apartment_price = 68.70

elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if count_nights > 14:
    apartment_price = apartment_price * 0.9

print(f'Apartment: {(count_nights * apartment_price):.2f} lv.')
print(f'Studio: {(count_nights * studio_price):.2f} lv.')
