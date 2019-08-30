town = input()
volume_trades = float(input())
commision = 0

if volume_trades < 0:
    print('error')
else:
    if town == 'Sofia':
        if 0 <= volume_trades and volume_trades <= 500:
            commision += volume_trades * 5 / 100

        elif 500 < volume_trades and volume_trades <= 1000:
            commision += volume_trades * 7 / 100

        elif 1000 < volume_trades and volume_trades <= 10000:
            commision += volume_trades * 8 / 100

        else:
            commision += volume_trades * 12 / 100

        print(f'{commision:.2f}')

    elif town == 'Varna':
        if 0 <= volume_trades and volume_trades <= 500:
            commision += volume_trades * 4.5 / 100

        elif 500 < volume_trades and volume_trades <= 1000:
            commision += volume_trades * 7.5 / 100

        elif 1000 < volume_trades and volume_trades <= 10000:
            commision += volume_trades * 10 / 100

        else:
            commision += volume_trades * 13 / 100

        print(f'{commision:.2f}')

    elif town == 'Plovdiv':
        if 0 <= volume_trades and volume_trades <= 500:
            commision += volume_trades * 5.5 / 100

        elif 500 < volume_trades and volume_trades <= 1000:
            commision += volume_trades * 8 / 100

        elif 1000 < volume_trades and volume_trades <= 10000:
            commision += volume_trades * 12 / 100

        else:
            commision += volume_trades * 14.5 / 100

        print(f'{commision:.2f}')

    else:
        print('error')