size = int(input())
bombs_number = int(input())

positions = {
    0: [-1, 0],  # up
    1: [1, 0],  # down
    2: [0, -1],  # left
    3: [0, 1],  # right
    4: [-1, -1],
    5: [-1, 1],
    6: [1, -1],
    7: [1, 1],
}
matrix = [[0 for _ in range(size)] for _ in range(size)]


def check(r, c):
    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "*":
            return False
        return True


def add(current_row, current_col):
    matrix[current_row][current_col] = "*"
    for key in range(8):
        roww, coll = current_row, current_col
        roww += positions[key][0]
        coll += positions[key][1]
        if check(roww, coll):
            matrix[roww][coll] += 1


for _ in range(bombs_number):
    pos_bomb = input()[1:-1].split(", ")
    row = int(pos_bomb[0])
    col = int(pos_bomb[1])
    add(row, col)

[print(*x) for x in matrix]
