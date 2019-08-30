class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, legs):
        Animal.__init__(self, name, age)
        self.legs = legs

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient):
        Animal.__init__(self, name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")


class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient):
        Animal.__init__(self, name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")


cats = []
dogs = []
snakes = []

line = input()

while not line == "I'm your Huckleberry" or line == "talk":
    # {class} {name} {age} {parameter}
    split_line = line.split()
    if len(split_line) == 4:
        the_class = split_line[0]
        name = split_line[1]
        age = split_line[2]
        parameter = split_line[3]

        if the_class == "Cat":
            cats.append(Cat(name, age, parameter))
        elif the_class == "Dog":
            dogs.append(Dog(name, age, parameter))
        else:
            snakes.append(Snake(name, age, parameter))

    elif split_line[0] == "talk":
        name_one = split_line[1]
        type_animal = False
        for cat in cats:
            if cat.name == name_one:
                cat.produce_sound()
                type_animal = True
                break
        if not type_animal:
            for dog in dogs:
                if dog.name == name_one:
                    dog.produce_sound()
                    type_animal = True
                    break
        if not type_animal:
            for snake in snakes:
                if snake.name == name_one:
                    snake.produce_sound()
                    type_animal = True
    line = input()

for dog in dogs:
    print(f"Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.legs}")

for cat in cats:
    print(f"Cat: {cat.name}, Age: {cat.age}, IQ: {cat.intelligence_quotient}")

for snake in snakes:
    print(f"Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.cruelty_coefficient}")
