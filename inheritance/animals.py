from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, typee, name, age: int, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.typee = typee

    @abstractmethod
    def produce_sound(self):
        pass

    def __str__(self):
        return f"{self.typee}\n{self.name} {self.age} {self.gender}\n{(self.produce_sound())}"


class Dog(Animal):
    def __init__(self, typee, name, age, gender):
        Animal.__init__(self, typee, name, age, gender)

    def produce_sound(self):
        return "Woof!"


class Frog(Animal):
    def __init__(self, typee, name, age, gender):
        Animal.__init__(self, typee, name, age, gender)

    def produce_sound(self):
        return "Ribbit"


class Cat(Animal):
    def __init__(self, typee, name, age, gender):
        Animal.__init__(self, typee, name, age, gender)

    def produce_sound(self):
        return "Meow meow"


class Kitten(Cat):
    def __init__(self, typee, name, age, gender="Female"):
        Cat.__init__(self, typee, name, age, gender)

    def produce_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, typee, name, age, gender="Male"):
        Cat.__init__(self, typee, name, age, gender)

    def produce_sound(self):
        return "MEOW"


animals = []
line = input()
while not line == "Beast!":
    typee = line
    line_two = input().split()
    name = line_two[0]
    age = int(line_two[1])
    gender = line_two[2]
    if not (typee == "Dog" or typee == "Cat" or typee == "Frog" or typee == "Tomcat" or typee == "Kitten") or (age < 0):
        print("Invalid input!")
    else:
        if typee == "Dog":
            animal = Dog(typee, name, age, gender)
        elif typee == "Frog":
            animal = Frog(typee, name, age, gender)
        elif typee == "Cat":
            animal = Cat(typee, name, age, gender)
        elif typee == "Tomcat":
            animal = Tomcat(typee, name, age)
        else:
            animal = Kitten(typee, name, age)
        animals.append(animal)
    line = input()

for animal in animals:
    print(animal)
