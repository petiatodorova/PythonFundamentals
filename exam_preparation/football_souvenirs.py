team_name = input()
souvenir_name = input()
count_souvenirs = int(input())
total_sum = 0

if not (team_name == "Argentina" or team_name == "Brazil" or team_name == "Croatia" or team_name == "Denmark"):
    print(f'Invalid country!')
elif not (souvenir_name == "flags" or souvenir_name == "caps" or souvenir_name == "posters" or souvenir_name == "stickers"):
    print('Invalid stock!')
else:
    if team_name == "Argentina":
        if souvenir_name == "flags":
            total_sum = count_souvenirs * 3.25
        elif souvenir_name == "caps":
            total_sum = count_souvenirs * 7.20
        elif souvenir_name == "posters":
            total_sum = count_souvenirs * 5.10
        elif souvenir_name == "stickers":
            total_sum = count_souvenirs * 1.25
    elif team_name == "Brazil":
        if souvenir_name == "flags":
            total_sum = count_souvenirs * 4.20
        elif souvenir_name == "caps":
            total_sum = count_souvenirs * 8.50
        elif souvenir_name == "posters":
            total_sum = count_souvenirs * 5.35
        elif souvenir_name == "stickers":
            total_sum = count_souvenirs * 1.20
    elif team_name == "Croatia":
        if souvenir_name == "flags":
            total_sum = count_souvenirs * 2.75
        elif souvenir_name == "caps":
            total_sum = count_souvenirs * 6.90
        elif souvenir_name == "posters":
            total_sum = count_souvenirs * 4.95
        elif souvenir_name == "stickers":
            total_sum = count_souvenirs * 1.10
    elif team_name == "Denmark":
        if souvenir_name == "flags":
            total_sum = count_souvenirs * 3.10
        elif souvenir_name == "caps":
            total_sum = count_souvenirs * 6.50
        elif souvenir_name == "posters":
            total_sum = count_souvenirs * 4.80
        elif souvenir_name == "stickers":
            total_sum = count_souvenirs * 0.90

    print(f'Pepi bought {count_souvenirs} {souvenir_name} of {team_name} for {total_sum:.2f} lv.')
