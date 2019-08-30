count_tables = int(input())
length_table = float(input())
width_table = float(input())

usd_price_rectangle_cover = 7;
usd_price_quadrat_cover = 9;

usd_price_rectangle_covers = (length_table + 0.60) * (width_table + 0.60) * usd_price_rectangle_cover * count_tables;
usd_price_quadrat_covers = (length_table / 2) **2 * usd_price_quadrat_cover * count_tables;

usd_total_price = usd_price_rectangle_covers + usd_price_quadrat_covers
bgn_total_price = usd_total_price * 1.85

print(f'{usd_total_price:.2f} USD')
print(f'{bgn_total_price:.2f} BGN')