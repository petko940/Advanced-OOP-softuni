def even_numbers(function):
    def wrapper(numbers):
        numbers = function(numbers)
        result = list(x for x in numbers if x % 2 == 0)
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
