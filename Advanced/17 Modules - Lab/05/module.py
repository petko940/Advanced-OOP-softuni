def fibonacci_sequence(number):
    fibonacci = []
    number1 = 0
    number2 = 1
    fibonacci.append(number1)
    fibonacci.append(number2)
    for _ in range(number - 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        number1 += number2
    return ' '.join([str(x) for x in fibonacci])


def check_sequence(number):
    numbers = fibonacci_sequence(number)
    for index, num in enumerate(numbers):
        if number == num:
            return f"The number - {number} is at index {index}"
    else:
        return f"The number {number} is not in the sequence"
