first_list = list(map(int, input().split()))
command = input()
results = []

while not command == "END":
    nums = first_list
    commands_line = command.split()
    if len(commands_line) == 3 and commands_line[0] == "multiply":
        # OK
        if not commands_line[1].isdigit():
            new = []
            n = int(commands_line[2])
            for el in nums:
                for m in range(n):
                    new.append(el)
            results.extend(new)

        else:
            # OK
            element = int(commands_line[1])
            n = int(commands_line[2])
            new = []
            for el in nums:
                if el == element:
                    new.append(el * n)
            results.extend(new)

    elif len(commands_line) == 2:
        # OK
        if commands_line[0] == "contains":
            num_to_check = int(commands_line[1])
            if nums.__contains__(num_to_check):
                results.append("True")
            else:
                results.append("False")



        elif commands_line[0] == "add":

            if commands_line[1].isdigit():
                # OK
                results.append(commands_line[1])
            else:
                '''{add} {n} – you should add n, where n could be a single 
                integer OR another list of integers (if n is a list it would be separated by ‘,’)'''
                results.extend(commands_line[1].split(","))


    command = input()

print(results)
for el in results:
    print(el, end=" ")
