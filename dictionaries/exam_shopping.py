line = input()

prod_quantity = {}

while not (line == 'shopping time'):
    line = line.split()
    key_product = line[1]
    value_product = int(line[2])
    if key_product in prod_quantity:
        prod_quantity[key_product] += value_product
    else:
        prod_quantity[key_product] = value_product
    line = input()

    '''buy {product} {quantity}'''
line = input()
while not (line == 'exam time'):
    line = line.split()
    key_to_buy = line[1]
    value_quantity = int(line[2])
    if not (key_to_buy in prod_quantity):
        print(f"{key_to_buy} doesn't exist")
    elif prod_quantity[key_to_buy] == 0:
        print(f"{key_to_buy} out of stock")
    elif prod_quantity[key_to_buy] <= value_quantity:
        prod_quantity[key_to_buy] = 0
    else:
        prod_quantity[key_to_buy] -= value_quantity

    line = input()

for key, value in prod_quantity.items():
    if value > 0:
        print(f'{key} -> {value}')