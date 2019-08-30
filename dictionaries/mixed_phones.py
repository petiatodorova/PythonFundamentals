line = input().split(" : ")

name_phone = {}

while not (line[0] == 'Over'):
    if not line[0].isdigit():
        key = line[0]
        value = line[1]
        name_phone[key] = value
    else:
        key = line[1]
        value = line[0]
        name_phone[key] = value
    line = input().split(" : ")

for key, value in sorted(name_phone.items()):
    print(f"{key} -> {value}")