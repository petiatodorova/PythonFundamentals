name = input()
age = int(input())
town = input()
salary = float(input())
ageRange = None
salaryRange = None

print(f'Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}')

if age < 18:
    ageRange = 'teen'
elif age < 70:
    ageRange = 'adult'
else:
    ageRange = 'elder'

if salary < 500:
    salaryRange = 'low'
elif salary < 2000:
    salaryRange = 'medium'
else:
    salaryRange = 'high'

print(f'Age range: {ageRange}\nSalary range: {salaryRange}')
