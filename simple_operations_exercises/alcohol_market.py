whiskey_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
brandy_liters = float(input())
whiskey_liters = float(input())

brandy_price = whiskey_price / 2
wine_price = brandy_price * 0.6
beer_price = brandy_price * 0.2

total_sum = whiskey_price * whiskey_liters \
            + beer_price * beer_liters \
            + wine_price * wine_liters \
            + brandy_price * brandy_liters

print(f'{total_sum:.2f}')