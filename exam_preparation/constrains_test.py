@property
def age(self):
    return self.__age

@age.setter
def age(self, value):
    if value < 0:
        raise Exception("Age must be positive!")
    else:
        self.__age = value