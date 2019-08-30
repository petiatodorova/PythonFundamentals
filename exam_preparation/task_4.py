from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, id, operating_system, price):
        self.id = id
        self.operating_system = operating_system
        self.price = float(price)


    @abstractmethod
    def __init__(self):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Invalid price!")
        else:
            self.__price = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def price(self, value):
        if not value.isalpha() or len(value) < 8:
            raise Exception("Invalid id!")
        else:
            self.__id = value


class Phone(ABC):
    def __init__(self, id, operating_system, price):
        self.id = int(id)
        self.operating_system = operating_system
        self.price = float(price)


    @abstractmethod
    def __init__(self):
        pass


class SmartPhone(Phone):
    def __init__(self, id, operating_system, price, apps):
        Phone.__init__(self, id, operating_system, price)
        self.apps = apps


    def __str__(self):
        return Phone.__str__(self)


'''SmartPhone("{id}", "{operating_system}", {price}, ["{app1}", "{app2}", "{app3}"…])
CellPhone("{id}", "{operating_system}", {price})
Tablet("{id}", "{operating_system}", {price})'''

class CellPhone(Phone):
    def __init__(self, id, operating_system, price):
        Phone.__init__(self, id, operating_system, price)

    def __str__(self):
        return Phone.__str__(self)


class Tablet(Item):
    def __init__(self, id, operating_system, price):
        Item.__init__(self, id, operating_system, price)

    def __str__(self):
        return Item.__str__(self)


data = input()
devices_list = []

while not data == "end":
    try:
        current_item = eval(data)
        devices_list.append(current_item)
    except Exception as ex:
        print(ex)

    data = input()


