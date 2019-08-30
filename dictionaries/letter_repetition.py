line = input()

dict_characters = {}

for item in line:
    if item in dict_characters:
        dict_characters[item] += 1
    else:
        dict_characters[item] = 1

for el in dict_characters:
    print(f"{el} -> {dict_characters[el]}")