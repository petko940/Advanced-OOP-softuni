def check(row, col, current_knights):
    # up left
    count = 0
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == "K":
            count += 1
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == "K":
            count += 1
    # up right
    if row - 2 >= 0 and col + 1 < size:
        if matrix[row - 2][col + 1] == "K":
            count += 1
    if row - 1 >= 0 and col + 2 < size:
        if matrix[row - 1][col + 2] == "K":
            count += 1
    # down left
    if row + 1 < size and col - 2 >= 0:
        if matrix[row + 1][col - 2] == "K":
            count += 1
    if row + 2 < size and col - 1 >= 0:
        if matrix[row + 2][col - 1] == "K":
            count += 1
    # down right
    if row + 2 < size and col + 1 < size:
        if matrix[row + 2][col + 1] == "K":
            count += 1
    if row + 1 < size and col + 2 < size:
        if matrix[row + 1][col + 2] == "K":
            count += 1
    current_knights[f"{row} {col}"] += count


def new():
    knights = {}
    knight_row = 0
    knight_col = 0
    for k in range(size):
        for index, knight in enumerate(matrix[k]):
            if "K" in knight:
                knight_row = k
                knight_col = index
                knights[f"{knight_row} {knight_col}"] = 0
                check(knight_row, knight_col, knights)
    return knights


size = int(input())
matrix = []
for i in range(size):
    matrix.append([x for x in input()])

removed = 0
while True:
    knights = new()
    if sum(knights.values()):
        for key, value in sorted(knights.items(), key=lambda x: -x[1]):
            r, c = [int(x) for x in key.split()]
            matrix[r][c] = "0"
            break
        removed += 1
    elif sum(knights.values()) == 0:
        break

print(removed)
