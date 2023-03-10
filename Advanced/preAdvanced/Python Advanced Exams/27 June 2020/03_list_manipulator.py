def list_manipulator(*args):
    list_of_numbers = args[0]
    where = args[2]
    numbers = []
    if len(args) > 3:
        for x in args[3:]:
            numbers.append(x)
    if args[1] == "add":
        if where == "beginning":
            for n in numbers[::-1]:
                list_of_numbers.insert(0, n)
        else:
            for n in numbers:
                list_of_numbers.append(n)
    elif args[1] == "remove":
        if where == "beginning":
            if numbers:
                list_of_numbers = list_of_numbers[numbers[0]:]
            else:
                list_of_numbers = list_of_numbers[1:]
        else:
            if numbers:
                list_of_numbers = list_of_numbers[:-numbers[0]]
            else:
                list_of_numbers = list_of_numbers[:-1]

    return list_of_numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
