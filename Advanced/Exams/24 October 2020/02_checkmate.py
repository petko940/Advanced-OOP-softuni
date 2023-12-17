matrix = [[x for x in input().split()] for _ in range(8)]

directions = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # top left
    (-1, 1),  # top right
    (1, -1),  # bot left
    (1, 1),  # bot right
]


def check_bounds(r, c):
    if 0 <= r < 8 and 0 <= c < 8:
        return True
    return False


position_queens = []
for row in range(8):
    for col in range(8):
        if matrix[row][col] == "Q":
            for direction in directions:
                r = row + direction[0]
                c = col + direction[1]
                while check_bounds(r, c):
                    if matrix[r][c] == "K":
                        position_queens.append(f"[{row}, {col}]")
                    elif matrix[r][c] == "Q":
                        break
                    r += direction[0]
                    c += direction[1]

if position_queens:
    [print(*x, sep="") for x in position_queens]
else:
    print('The king is safe!')
