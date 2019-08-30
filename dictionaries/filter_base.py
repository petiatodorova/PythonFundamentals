input_line = input()

name_age = {}
name_salary = {}
name_position = {}

while not input_line == "filter base":
    line = input_line.split(' -> ')
    key = line[0]
    value = line[1]

    try:
        int(value)
        name_age[key] = value
    except:
        try:
            float(value)
            name_salary[key] = value
        except:
            name_position[key] = value

    input_line = input()

last_string = input()

if last_string == 'Age':
    for name, age in name_age.items():
        print(f"Name: {name}")
        print(f"Age: {age}")
        print("====================")
elif last_string == 'Salary':
    for name, salary in name_salary.items():
        print(f"Name: {name}")
        print(f"Salary: {salary}")
        print("====================")
else:
    for name, position in name_position.items():
        print(f"Name: {name}")
        print(f"Position: {position}")
        print("====================")

