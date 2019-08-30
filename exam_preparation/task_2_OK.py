# first_list = list(map(int, input().split()))
nums = list(map(int, input().split()))
command = input()
results = []
lst_true = []
lst_false = []
while not command == "END":
    # nums = first_list
    commands_line = command.split()
    if len(commands_line) == 3 and commands_line[0] == "multiply":
        if not commands_line[1].isdigit():
            new = []
            n = int(commands_line[2])
            for el in nums:
                for m in range(n):
                    new.append(el)
            results.extend(new)
        else:
            element = int(commands_line[1])
            n = int(commands_line[2])
            new = []
            for el in nums:
                if el == element:
                    new.append(el * n)
            results.extend(new)

    elif len(commands_line) == 2:
        if commands_line[0] == "contains":
            num_to_check = int(commands_line[1])
            if nums.__contains__(num_to_check):
                lst_true.append("True")
            else:
                lst_false.append("False")
        elif commands_line[0] == "add":
            if commands_line[1].isdigit():
                results.append(commands_line[1])
            else:
                results.extend(commands_line[1].split(","))
    command = input()

if len(lst_true) > 0:
    print(" ".join(lst_true), end=" ")
if len(lst_false) > 0:
    print(" ".join(lst_false), end=" ")
results = sorted(map(int, results))
results = map(str, results)
print(" ".join(results), end=" ")