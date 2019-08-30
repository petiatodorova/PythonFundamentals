class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staff_number = staffnum


    def get_employee(self):
        return f"{self.get_name()} {self.staff_number}"


person = Person("Mimi", "Todorova")
employee = Employee("Gosho", "Georgiev", 22)

print(f"Employee get name {employee.get_name()}")
print(f"Employee get employee {employee.get_employee()}")
print(f"Person get name {person.get_name()}")