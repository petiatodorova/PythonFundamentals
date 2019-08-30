class Person:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age must be positive!")
        else:
            self.__age = value

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 15:
            raise Exception("Child's age must be less than 15!")
        if value < 0:
            raise Exception("Age must be positive!")
        else:
            self.__age = value


name = input()
age = int(input())
try:
    chld = Child(name, age)
    print(chld)
except Exception as e:
    print(e)
