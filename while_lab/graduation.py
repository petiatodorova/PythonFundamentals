name = input()
count = 12
total_grade = 0

while count > 0:
    current_grade = float(input())

    if current_grade >= 4.00:
        count -= 1
        total_grade += current_grade

average_grade = total_grade / 12

if count == 0:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')