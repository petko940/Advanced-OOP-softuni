try:
    file = open('numbers.txt', "r")

    numbers_sum = [int(x) for x in file.read() if x.isdigit()]
    print(sum(numbers_sum))
except FileNotFoundError:
    print("File not found")
