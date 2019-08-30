PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

vacation_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

total_sum = PUZZLE_PRICE * count_puzzles \
            + DOLL_PRICE * count_dolls \
            + BEAR_PRICE * count_bears \
            + MINION_PRICE * count_minions \
            + TRUCK_PRICE * count_trucks

total_toys_count = count_trucks + count_minions + count_bears + count_dolls + count_puzzles

if total_toys_count >= 50:
    total_sum = total_sum * 0.75

total_sum = total_sum * 0.90

money_diff = abs(total_sum - vacation_price)

if total_sum >= vacation_price:
    print(f'Yes! {money_diff:.2f} lv left.')
else:
    print(f'Not enough money! {money_diff:.2f} lv needed.')