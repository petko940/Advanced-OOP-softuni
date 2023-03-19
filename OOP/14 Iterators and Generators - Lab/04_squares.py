def squares(number):
    for i in range(1, number + 1):
        yield i ** 2


print(list(squares(5)))