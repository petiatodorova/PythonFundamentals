count_sectors = int(input())
capacity = int(input())
ticket_price = float(input())

total_income = capacity * ticket_price
money_for_charity = (total_income - (total_income / count_sectors * 0.75)) / 8

print(f'Total income - {total_income:.2f} BGN')
print(f'Money for charity - {money_for_charity:.2f} BGN')