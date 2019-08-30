data = input()
if len(data) > 0:
    nums = list(map(int, data.split()))
    command = input()
    lst_true = []
    lst_false = []

    while not command == "END":
        commands_line = command.split()
        if len(commands_line) == 3 and commands_line[0] == "multiply":
            if not commands_line[1].isdigit() and type(commands_line[2] == list):
                n = int(commands_line[2])
                nums = nums * n

            else:
                element = int(commands_line[1])
                n = int(commands_line[2])

                for m in range(len(nums)):
                    if nums[m] == element:
                        nums[m] = nums[m] * n

        elif len(commands_line) == 2:
            if commands_line[0] == "contains":
                num_to_check = int(commands_line[1])
                if num_to_check in nums:
                    lst_true.append("True")
                else:
                    lst_false.append("False")

            elif commands_line[0] == "add":

                if commands_line[1].isdigit():
                    nums.append(commands_line[1])
                else:
                    nums.extend(commands_line[1].split(","))
        else:
            pass
        command = input()

    if len(lst_true) > 0:
        for el in lst_true:
            print(el)
    if len(lst_false) > 0:
        for el_1 in lst_false:
            print(el_1)
    nums = sorted(map(int, nums))
    nums = map(str, nums)
    print(" ".join(nums), end=" ")

