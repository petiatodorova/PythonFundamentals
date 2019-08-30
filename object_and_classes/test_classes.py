class A:

    def __init__(self, name):
        self.name = name

    def func1(self):
        print("func1")

    def func2(self):
        print("func2")


class B(A):

    def func3(self):
        print("func3")

    def func4(self):
        print("func4")


bclass = B("Mimi")
print(bclass.name)
bclass.func4()