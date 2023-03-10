def new_position(direction, pos_row, pos_col):
    pos_row += directions[direction]["row"]
    pos_col += directions[direction]["col"]
    return pos_row, pos_col


def create(direction, value, pos_row, pos_col):
    pos_row, pos_col = new_position(direction, pos_row, pos_col)
    if matrix[pos_row][pos_col] == ".":
        matrix[pos_row][pos_col] = value
    return pos_row, pos_col


def update(direction, value, pos_row, pos_col):
    pos_row, pos_col = new_position(direction, pos_row, pos_col)
    if matrix[pos_row][pos_col] != ".":
        matrix[pos_row][pos_col] = value
    return pos_row, pos_col


def delete(direction, pos_row, pos_col):
    pos_row, pos_col = new_position(direction, pos_row, pos_col)
    if matrix[pos_row][pos_col] != ".":
        matrix[pos_row][pos_col] = "."
    return pos_row, pos_col


def read(direction, pos_row, pos_col):
    pos_row, pos_col = new_position(direction, pos_row, pos_col)
    if matrix[pos_row][pos_col] != ".":
        print(matrix[pos_row][pos_col])
    return pos_row, pos_col


size = 6
matrix = [[x for x in input().split()] for x in range(size)]
my_pos = input().split(", ")
my_pos_row, my_pos_col = int(my_pos[0][1:]), int(my_pos[1][:-1])

directions = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}
while True:
    commands = input()
    if commands == "Stop":
        break
    event, direction, *value = commands.split(", ")
    if event == "Create":
        my_pos_row, my_pos_col = create(direction, value[0], my_pos_row, my_pos_col)
    elif event == "Update":
        my_pos_row, my_pos_col = update(direction, value[0], my_pos_row, my_pos_col)
    elif event == "Delete":
        my_pos_row, my_pos_col = delete(direction, my_pos_row, my_pos_col)
    elif event == "Read":
        my_pos_row, my_pos_col = read(direction, my_pos_row, my_pos_col)

# for row in matrix:
#     print(*row)
[print(*row) for row in matrix]
