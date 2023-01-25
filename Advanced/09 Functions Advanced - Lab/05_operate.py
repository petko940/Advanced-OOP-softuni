from functools import reduce


def operate(operator, *args):
    def add():
        return reduce(lambda x, y: x + y, args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def division():
        return reduce(lambda x, y: x / y, args)

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
