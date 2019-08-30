line = input().split(" = ")

dict_ref = {}

while line[0] != "end":
    key = line[0]
    value = line[1]
    if value.isdigit():
        dict_ref[key] = int(value)
    elif value in dict_ref:
        dict_ref[key] = int(dict_ref[value])
    line = input().split(" = ")

for item in dict_ref:
    print(f"{item} === {dict_ref[item]}")
