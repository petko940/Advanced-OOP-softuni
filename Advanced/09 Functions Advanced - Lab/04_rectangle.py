def rectangle(*args):
    def perimeter(length, width):
        return 2 * (length + width)

    def area(length, width):
        return length * width

    if type(args[0]) != str and type(args[1]) != str:
        return f"Rectangle area: {area(*args)}\nRectangle perimeter: {perimeter(*args)}"
    else:
        return "Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))
