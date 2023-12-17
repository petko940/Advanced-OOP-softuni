directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'topleft': (-1, -1),
    'topright': (-1, 1),
    'downleft': (1, -1),
    'downright': (1, 1),
}

size = int(input())
matrix = [[0 for x in range(size)] for _ in range(size)]

for _ in range(int(input())):
    bomb_pos = input().split(', ')
    bomb_row, bomb_col = int(bomb_pos[0][1:]), int(bomb_pos[1][:-1])
    matrix[bomb_row][bomb_col] = "*"


def check_directions(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


for row in range(size):
    for col in range(size):
        if matrix[row][col] == "*":
            for x, y in directions.values():
                if check_directions(row + x, col + y) and matrix[row + x][col + y] != "*":
                    matrix[row + x][col + y] += 1

[print(*x) for x in matrix]
