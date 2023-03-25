def cache(func):
    def wrapper(number):
        if number not in wrapper.log:
            wrapper.log[number] = func(number)

        return wrapper.log[number]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

