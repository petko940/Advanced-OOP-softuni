# jetfighter = J
# enemy airplane = E
# repair = R
# empty = "-"

size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

jetfighter_armor = 300
enemies_count = 4

jetfighter_pos = None

for r in range(size):
    if "J" in matrix[r]:
        jetfighter_pos = (r, matrix[r].index("J"))
        matrix[r][matrix[r].index("J")] = "-"

# (row, column)
matrix_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    row, col = jetfighter_pos
    new_row, new_col = row + matrix_directions[command][0], col + matrix_directions[command][1]

    if matrix[new_row][new_col] == "E":
        matrix[new_row][new_col] = "-"
        enemies_count -= 1
        if enemies_count == 0:
            matrix[new_row][new_col] = "J"
            break

        jetfighter_armor -= 100
        if jetfighter_armor == 0:
            matrix[new_row][new_col] = "J"
            break

    elif matrix[new_row][new_col] == "R":
        jetfighter_armor = 300
        matrix[new_row][new_col] = "-"

    jetfighter_pos = (new_row, new_col)

if not enemies_count:
    print(f"Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")

[print("".join(x)) for x in matrix]
