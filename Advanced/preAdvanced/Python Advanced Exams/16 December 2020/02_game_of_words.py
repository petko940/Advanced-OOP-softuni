string = input()
size = int(input())
matrix = [[x for x in input()] for x in range(size)]

position = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}
row, col = 0, 0
for i in range(size):
    if "P" in matrix[i]:
        row = i
        col = matrix[i].index("P")


def move(current_row, current_col, str):
    matrix[current_row][current_col] = "-"
    current_row += position[command]["row"]
    current_col += position[command]["col"]
    if not (0 <= current_row < size):
        if current_row < 0:
            current_row = 0
        else:
            current_row = size - 1
        str = str[:-1]
    elif not (0 <= current_col < size):
        if current_col < 0:
            current_col = 0
        else:
            current_col = size - 1
        str = str[:-1]
    elif matrix[current_row][current_col] != "-":
        str += matrix[current_row][current_col]
    matrix[current_row][current_col] = "P"
    return current_row, current_col, str


moves = int(input())
for _ in range(moves):
    command = input()
    row, col, string = move(row, col, string)

print(string)
[print(*x, sep="") for x in matrix]
