days_count = int(input())
room_type = input()
rating = input()

PRICE_ONE_PERSON = 18.00
PRICE_APARTMENT = 25.00
PRICE_PRESIDENT_APARTMENT = 35.00

total_price = 0
days_count -= 1

if days_count < 10:
    if room_type == 'room for one person':
        total_price = days_count * PRICE_ONE_PERSON
    elif room_type == 'apartment':
        total_price = days_count * PRICE_APARTMENT * 0.70
    elif room_type == 'president apartment':
        total_price = days_count * PRICE_PRESIDENT_APARTMENT * 0.90

elif 10 <= days_count and days_count <= 15:
    if room_type == 'room for one person':
        total_price = days_count * PRICE_ONE_PERSON
    elif room_type == 'apartment':
        total_price = days_count * PRICE_APARTMENT * 0.65
    elif room_type == 'president apartment':
        total_price = days_count * PRICE_PRESIDENT_APARTMENT * 0.85

else:
    if room_type == 'room for one person':
        total_price = days_count * PRICE_ONE_PERSON
    elif room_type == 'apartment':
        total_price = days_count * PRICE_APARTMENT * 0.50
    elif room_type == 'president apartment':
        total_price = days_count * PRICE_PRESIDENT_APARTMENT * 0.80

if rating == 'positive':
    total_price += total_price * 0.25
elif rating == 'negative':
    total_price = total_price * 0.90

print(f'{total_price:.2f}')