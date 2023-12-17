rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]
# [print(*x) for x in matrix]
"""
me = B
obstacles = O
opponents = P
"""
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

pos = []
for i in range(rows):
    if 'B' in matrix[i]:
        pos = [i, matrix[i].index("B")]
        matrix[i][pos[1]] = '-'


def check_out_field(r, c):
    if 0 <= r < rows and 0 <= c < columns:
        return True
    return False


touched_opponents, moves = 0, 0
row, col = pos[0], pos[1]
while True:
    cmd = input()
    if cmd.startswith('Finish'):
        break

    if check_out_field(row + directions[cmd][0], col + directions[cmd][1]):
        if matrix[row + directions[cmd][0]][col + directions[cmd][1]] == "O":
            continue
        row += directions[cmd][0]
        col += directions[cmd][1]
        if matrix[row][col] == "P":
            touched_opponents += 1
            moves += 1
            if touched_opponents == 3:
                break
            matrix[row][col] = "-"
        elif matrix[row][col] == "-":
            moves += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
