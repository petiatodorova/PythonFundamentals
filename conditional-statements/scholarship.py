import math

income = float(input())
average_success = float(input())
min_salary = float(input())
social_scholarship = math.floor(min_salary * 0.35)
excellent_scholarship = math.floor((average_success * 25))

if average_success < 4.5:
    print('You cannot get a scholarship!')
elif average_success < 5.5:
    if income >= min_salary:
        print('You cannot get a scholarship!')
    else:
        print(f'You get a Social scholarship {social_scholarship:.0f} BGN')
else:
    if income >= min_salary:
        print(f'You get a scholarship for excellent results {excellent_scholarship:.0f} BGN')
    else:
        if excellent_scholarship >= social_scholarship:
            print(f'You get a scholarship for excellent results {excellent_scholarship:.0f} BGN')
        else:
            print(f'You get a Social scholarship {social_scholarship:.0f} BGN')






