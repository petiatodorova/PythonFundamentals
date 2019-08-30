class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # first name validator
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if not value[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        elif not (len(value) > 3):
            raise Exception("Expected length at least 4 symbols! Argument: firstName")
        else:
            self.__first_name = value

    # last name validator
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        elif not (len(value) > 2):
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        else:
            self.__last_name = value


class Worker(Human):
    def __init__(self, first_name, last_name, week_salary: float, work_hours_per_day: float):
        Human.__init__(self, first_name, last_name)
        self.week_salary = week_salary
        self.work_hours_per_day = work_hours_per_day

    # week salary validator
    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, value):
        if value <= 10:
            raise Exception("Expected value mismatch! Argument: weekSalary")
        else:
            self.__week_salary = value

    # working hours validator
    @property
    def work_hours_per_day(self):
        return self.__work_hours_per_day

    @work_hours_per_day.setter
    def work_hours_per_day(self, value):
        if value < 1 or value > 12:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")
        else:
            self.__work_hours_per_day = value

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nWeek Salary: {self.week_salary:.2f}\n" \
               f"Hours per day: {self.work_hours_per_day:.2f}\n" \
               f"Salary per hour: {self.week_salary / (5 * self.work_hours_per_day):.2f}"


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    # faculty_number validator
    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, value):
        symbols = list(filter(lambda x: not (x.isdigit() or x.isalpha()), value))
        if not (5 < len(value) < 10) or len(symbols) > 0:
            raise Exception("Invalid faculty number!")
        else:
            self.__faculty_number = value

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_number}\n"


single_student = input().split()
st_first_name = single_student[0]
st_last_name = single_student[1]
st_fac_number = single_student[2]

single_worker = input().split()
w_first_name = single_worker[0]
w_last_name = single_worker[1]
w_week_salary = float(single_worker[2])
w_work_hours_per_day = float(single_worker[3])

try:
    student = Student(st_first_name, st_last_name, st_fac_number)
    worker = Worker(w_first_name, w_last_name, w_week_salary, w_work_hours_per_day)
    print(student)
    print(worker)
except Exception as e:
    print(e)
