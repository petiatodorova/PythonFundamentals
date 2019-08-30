line = [word.lower() for word in input().split()]

dict_words = {}

for item in line:
    if item in dict_words:
        dict_words[item] += 1
    else:
        dict_words[item] = 1

result = []

for el in dict_words:
    if dict_words[el] % 2 == 1:
        result.append(el)

print(", ".join(result))
