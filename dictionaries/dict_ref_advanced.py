line = input().split(" -> ")

key_val = {}

while not line[0] == "end":
    name = line[0]
    item = line[1].split(", ")
    if item[0].isdigit():
        if name not in key_val.keys():
            key_val[name] = []
        key_val[name].extend(item)
    else:
        if item[0] in key_val.keys():
            if name not in key_val.keys():
                key_val[name] = []
            key_val[name].extend(key_val[item[0]])

    line = input().split(" -> ")

for key, val in key_val.items():
    val_str = ", ".join(val)
    print(f"{key} === {val_str}")
