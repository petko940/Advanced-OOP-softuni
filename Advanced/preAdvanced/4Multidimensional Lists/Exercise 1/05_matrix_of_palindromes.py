from string import ascii_lowercase as x

rows, columns = [int(x) for x in input().split()]
index = 0
middle_index = 0
for row in range(rows):
    for col in range(columns):
        print(f"{x[index]}{x[middle_index]}{x[index]}", end=" ")
        middle_index += 1
    index += 1
    middle_index = index
    print()
