"""
    • * - a regular position on the field
    • e - the end of the route
    • c - coal
    • s - miner
"""
size = int(input())
commands = input().split()

start_row_index = 0
start_col_index = 0
matrix = []
coal_count = 0
# fill matrix and find start locatioin
for i in range(size):
    matrix.append([x for x in input().split()])
    if "s" in matrix[i]:
        for x in matrix[i]:
            if x == "s":
                start_row_index = i
                start_col_index = matrix[i].index("s")
                break

# number coals
for m in matrix:
    for coal in m:
        if coal == "c":
            coal_count += 1


def check_up(matrix, count, exit):
    if matrix[start_row_index - 1][start_col_index] == "e":
        exit.append(1)
        return exit
    elif matrix[start_row_index - 1][start_col_index] == "c":
        count += 1
        matrix[start_row_index - 1][start_col_index] = "*"
    return count


def check_down(matrix, count, exit):
    if matrix[start_row_index + 1][start_col_index] == "e":
        exit.append(1)
        return exit
    elif matrix[start_row_index + 1][start_col_index] == "c":
        count += 1
        matrix[start_row_index + 1][start_col_index] = "*"
    return count


def check_left(matrix, count, exit):
    if matrix[start_row_index][start_col_index - 1] == "e":
        exit.append(1)
        return exit
    elif matrix[start_row_index][start_col_index - 1] == "c":
        count += 1
        matrix[start_row_index][start_col_index - 1] = "*"
    return count


def check_right(matrix, count, exit):
    if matrix[start_row_index][start_col_index + 1] == "e":
        exit.append(1)
        return exit
    elif matrix[start_row_index][start_col_index + 1] == "c":
        count += 1
        matrix[start_row_index][start_col_index + 1] = "*"
    return count


collected_coal = 0
check_end = []
# moving
for command in commands:
    if command == "up":
        if 0 <= start_row_index - 1:
            collected_coal = check_up(matrix, collected_coal, check_end)
            start_row_index -= 1
    elif command == "down":
        if start_row_index + 1 < size:
            collected_coal = check_down(matrix, collected_coal, check_end)
            start_row_index += 1
    elif command == "left":
        if 0 <= start_col_index - 1:
            collected_coal = check_left(matrix, collected_coal, check_end)
            start_col_index -= 1
    elif command == "right":
        if start_col_index + 1 < size:
            collected_coal = check_right(matrix, collected_coal, check_end)
            start_col_index += 1

    if collected_coal == coal_count:
        print("You collected all coal!", end=" ")
        print(f"({start_row_index}, {start_col_index})")
        break

    if check_end:
        print(f"Game over!", end=" ")
        print(f"({start_row_index}, {start_col_index})")
        break
else:
    print(f"{collected_coal} pieces of coal left.", end=" ")
    print(f"({start_row_index}, {start_col_index})")
