def operations(info):
    global sign, number1, number2
    try:
        data = info.split()
        number1, sign, number2 = float(data[0]), data[1], int(data[2])
        number2 = int(number2)
    except AttributeError:
        print("Enter string")

    operation = {
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
        "+": lambda x, y: x + y,
        "^": lambda x, y: x ** y,
    }
    a = operation[sign](number1, number2)
    return f"{a:.2f}"


