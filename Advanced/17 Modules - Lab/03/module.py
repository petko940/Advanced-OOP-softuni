def triangle(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for x in range(number - 1, 0, -1):
        for y in range(1, x + 1,):
            print(y, end=" ")
        print()

    return ""
