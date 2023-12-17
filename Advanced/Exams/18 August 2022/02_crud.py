matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(6)]
first_position = input()
row, col = int(first_position[1:2]), int(first_position[4:-1])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def check_if_position_is_empty(r, c):
    if matrix[r][c] == ".":
        return True
    return False


while True:
    commands = input()
    if commands == "Stop":
        break
    command, *data = commands.split(", ")
    row += directions[data[0]][0]
    col += directions[data[0]][1]
    if commands.startswith("Create"):
        if check_if_position_is_empty(row, col):
            matrix[row][col] = data[1]
    elif commands.startswith("Update"):
        if not check_if_position_is_empty(row, col):
            matrix[row][col] = data[1]
    elif commands.startswith("Delete"):
        matrix[row][col] = '.'
    elif commands.startswith("Read"):
        if not check_if_position_is_empty(row, col):
            print(matrix[row][col])

[print(*x) for x in matrix]
