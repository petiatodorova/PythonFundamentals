class Person:
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g


person_1 = Person("Petya", 32.5, "female")
person_2 = Person("Ines", 23.6, "female")

print(person_1.age + person_2.age)