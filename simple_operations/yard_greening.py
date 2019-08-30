quadrat_price = 7.61
percents_discount = 18 / 100
area = float(input())
final_price = area * quadrat_price * (1 - percents_discount)
discount_price = area * quadrat_price * percents_discount

print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount_price:.2f} lv.')