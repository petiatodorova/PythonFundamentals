days_count = int(input())
confectioners_count = int(input())
cakes_count = int(input())
wafer_count = int(input())
pancake_count = int(input())

price_cake = 45
price_wafer = 5.80
price_pancake = 3.20

one_confectioner_sum = cakes_count * price_cake + wafer_count * price_wafer + pancake_count * price_pancake
total_sum = (days_count * confectioners_count * one_confectioner_sum) * 7/8

print(f'{total_sum:.2f}')