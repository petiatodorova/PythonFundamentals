length = int(input())
width = int(input())
height = int(input())
percent_volume = float(input())

volume = length * width * height / 1000
water_liters = volume * (1 - percent_volume / 100)

print(f'{water_liters:.3f}')