def numbers_searching(*args):
    checked_numbers = []
    for arg in args:
        checked_numbers.append(arg)
    checked_numbers = sorted(checked_numbers)
    set_numbers = set(checked_numbers)
    missing_number = [x for x in range(checked_numbers[0], checked_numbers[0] + len(set_numbers)) if
                      x not in set_numbers]
    duplicates = [x for n, x in enumerate(checked_numbers) if x in checked_numbers[:n]]
    output = [missing_number[0], duplicates]
    return output


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
