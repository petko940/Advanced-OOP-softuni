def movements(cmd, x, y):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    x += moves[cmd][0]
    y += moves[cmd][1]
    return x, y


def check_bounds(x, y):
    x = (x + size) % size
    y = (y + size) % size
    return x, y


size = int(input())
matrix = [[x for x in input()] for row in range(size)]
pos_row, pos_col = 0, 0

for row in matrix:
    for r in row:
        if r == "S":
            pos_row, pos_col = matrix.index(row), row.index(r)
            matrix[pos_row][pos_col] = "-"
            break

result = None
passage = 0
is_done = False
is_break = False

while True:
    command = input()
    if command == "collect the nets":
        break
    pos_row, pos_col = movements(command, pos_row, pos_col)
    pos_row, pos_col = check_bounds(pos_row, pos_col)
    if matrix[pos_row][pos_col].isdigit():
        passage += int(matrix[pos_row][pos_col])
        matrix[pos_row][pos_col] = "-"
    elif matrix[pos_row][pos_col] == "W":
        is_break = True
        break

matrix[pos_row][pos_col] = "S"
if is_break:
    print(
        f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{pos_row},{pos_col}]")
else:
    if passage >= 20:
        print(f"Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - passage} tons of fish more.")

    if passage:
        print(f"Amount of fish caught: {passage} tons.")
    [print(*x, sep="") for x in matrix]
