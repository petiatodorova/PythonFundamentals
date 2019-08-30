remainder = float(input()) * 100

two_levs_count = remainder // 200
remainder -= two_levs_count * 200

one_lev_count = remainder // 100
remainder -= one_lev_count * 100

fifty_cents_count = remainder // 50
remainder -= fifty_cents_count * 50

twenty_cents_count = remainder // 20
remainder -= twenty_cents_count * 20

ten_cents_count = remainder // 10
remainder -= ten_cents_count * 10

five_cents_count = remainder // 5
remainder -= five_cents_count * 5

two_cents_count = remainder // 2
remainder -= two_cents_count * 2

one_cent_count = remainder // 1
remainder -= one_cent_count * 1

count_coins = two_levs_count + one_lev_count + fifty_cents_count \
              + twenty_cents_count + ten_cents_count + five_cents_count + two_cents_count + one_cent_count

print(f'{int(count_coins)}')
