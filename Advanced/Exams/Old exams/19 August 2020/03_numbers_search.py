def numbers_searching(*args):
    sorted_numbers = sorted(args)
    start_range, end_range = min(sorted_numbers), max(sorted_numbers)
    missing_number, duplicates = 0, []
    for i in range(start_range, end_range + 1):
        if i not in sorted_numbers:
            missing_number = i
        if sorted_numbers.count(i) > 1:
            duplicates.append(i)

    output = [missing_number, duplicates]
    return output


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(1, 2, 4, 2, 5, 4))
