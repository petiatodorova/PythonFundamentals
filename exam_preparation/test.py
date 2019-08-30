class Person:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise Exception("Age must be positive!")
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value.split()) > 1:
            second_name = value.split()[1]
            if not second_name.isalpha():
                raise Exception("Name must be from letters!")
        self.__name = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if not (value == "m" or value == "f"):
            raise Exception("Invalid gender!")
        self.__gender = value

    def __str__(self):
        return f"Class: {self.__class__.__name__}. Age is {self.age}.\nName is {self.name}.\nGender is {self.gender}."


try:
    person = Person(33, "Ivan ivanov", "m")
    print(person)
except Exception as e:
    print(e)

