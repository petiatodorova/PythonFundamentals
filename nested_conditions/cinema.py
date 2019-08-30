type_projection = input()
row_count = int(input())
column_count = int(input())

PREMIERE_PRICE = 12.00
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5.00

total_sum = 0

if type_projection.lower() == 'premiere':
    total_sum = row_count * column_count * PREMIERE_PRICE

elif type_projection.lower() == 'normal':
    total_sum = row_count * column_count * NORMAL_PRICE

elif type_projection.lower() == 'discount':
    total_sum = row_count * column_count * DISCOUNT_PRICE

print(f'{total_sum:.2f} leva')

