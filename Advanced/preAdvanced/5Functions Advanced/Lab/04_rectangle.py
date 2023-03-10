from numbers import Integral


def rectangle(length, width):
    if not (isinstance(length, Integral) and isinstance(width, Integral)):
        return "Enter valid values!"
    rectangle_area = area(length, width)
    rectangle_perimeter = perimeter(length, width)
    return f"Rectangle area: {rectangle_area}\nRectangle perimeter: {rectangle_perimeter}"


def area(l, w):
    return l * w


def perimeter(l, w):
    return 2 * (l + w)


print(rectangle(2, 10))
print(rectangle('2', 10))
