SIZE = int(input())
matrix = [[x for x in input()] for _ in range(SIZE)]

directions = {
    'up-left1': (-1, -2),
    'up-left2': (-2, -1),
    'up-right1': (-2, 1),
    'up-right2': (-1, 2),
    'down-left1': (1, -2),
    'down-left2': (2, -1),
    'down-right1': (2, 1),
    'down-right2': (1, 2),
}


def check(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True
    return False


max_knights = 0
max_knights_pos = None
removed_knights_count = 0
while True:
    for row in range(SIZE):
        for col in range(SIZE):
            current_knight_pos = (row, col)
            if matrix[row][col] == "K":
                current_knights = 0
                for values in directions.values():
                    r, c = row + values[0], col + values[1]
                    if check(r, c):
                        if matrix[r][c] == "K":
                            current_knights += 1
                if current_knights > max_knights:
                    max_knights = current_knights
                    max_knights_pos = current_knight_pos
    if max_knights == 0:
        print(removed_knights_count)
        break
    else:
        matrix[max_knights_pos[0]][max_knights_pos[1]] = '0'
        max_knights = 0
        max_knights_pos = None
        removed_knights_count += 1

