def operate(operator, *args):
    result = None
    if operator == "+":
        result = 0
        for arg in args:
            result += arg
    elif operator == "-":
        result = args[0]
        for arg in args[1:]:
            result -= arg
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
    elif operator == "/":
        result = args[0]
        for arg in args[1:]:
            result /= arg
    return result


print(operate("+", 1, 2, 3))
print(operate("-", 5, 3))
print(operate("*", 3, 4))
print(operate("/", 4, 4))
