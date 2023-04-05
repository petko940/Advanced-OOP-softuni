class test:
    def __init__(self, name):
        self.__name = name

    def asd(self):
        return self.__name


a = test("asd")
print(a.asd())
