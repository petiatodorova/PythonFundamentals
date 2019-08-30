name = input()
years_finished = 0
total_grade = 0
count_repetitions = 0

while years_finished < 12:
    current_grade = float(input())

    if current_grade >= 4.00:
        years_finished += 1
        total_grade += current_grade
    else:
        count_repetitions += 1
        if count_repetitions > 1:
            years_finished += 1
            break

if years_finished < 12:
    print(f'{name} has been excluded at {years_finished} grade')
else:
    average_grade = total_grade / 12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')