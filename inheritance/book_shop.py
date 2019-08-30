class Book:
    def __init__(self, title, author, price: float):
        self.title = title
        self.author = author
        self.price = price

    # title validation
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            raise Exception("Title not valid!")
        else:
            self.__title = value

    # author validation
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value: str):
        if (len(value.split()) > 1) and (value.split()[1][0].isdigit()):
            raise Exception("Author not valid!")
        else:
            self.__author = value

    # price validation
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Price not valid!")
        else:
            self.__price = value

    def __str__(self):
        return f"Type: Book\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}\n"


class GoldenEditionBook(Book):
    def __init__(self, title, author, price: float):
        Book.__init__(self, title, author, price)

    # price validation
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value * 1.30

    def __str__(self):
        return f"Type: GoldenEditionBook\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}"


author = input()
title = input()
price = float(input())

try:
    book = Book(title, author, price)
    golden_book = GoldenEditionBook(title, author, price)
    print(book)
    print(golden_book)
except Exception as e:
    print(e)
