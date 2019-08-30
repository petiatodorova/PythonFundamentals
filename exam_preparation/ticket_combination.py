combination_number = int(input())
count_valid_combinations = 0

for symbol_one in range (ord('B'), ord('L') + 1, 2):
    for symbol_two in range (ord('f'), ord('a') - 1, -1):
        for symbol_three in range(ord('A'), ord('C') + 1):
            for symbol_four in range(1, 11):
                for symbol_five in range(10, 0, -1):
                    count_valid_combinations += 1
                    if count_valid_combinations == combination_number:
                        ticket = chr(symbol_one) + chr(symbol_two) + chr(symbol_three) + str(symbol_four) + str(symbol_five)
                        prize = symbol_one + symbol_two + symbol_three + symbol_four + symbol_five
                        print(f'Ticket combination: {ticket}')
                        print(f'Prize: {prize} lv.')
                        break
