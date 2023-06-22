rows, cols = [int(x) for x in input().split(',')]

matrix = [[x for x in input()] for _ in range(rows)]

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

mouse_pos = []
cheese_pos = []
cheese_count = 0
for i in range(rows):
    if 'M' in matrix[i]:
        mouse_pos = [i, matrix[i].index('M')]
        matrix[i][mouse_pos[1]] = '*'
    cheese_count += matrix[i].count('C')


def in_matrix(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return True
    return False


while True:
    command = input()

    if command == 'danger':
        print(f"Mouse will come back later!")
        break

    try_row, try_col = mouse_pos[0] + direction[command][0], mouse_pos[1] + direction[command][1]

    if in_matrix(try_row, try_col):
        if matrix[try_row][try_col] == 'C':
            mouse_pos = [try_row, try_col]
            matrix[try_row][try_col] = '*'
            cheese_count -= 1
            if cheese_count == 0:
                print(f"Happy mouse! All the cheese is eaten, good night!")
                break

        elif matrix[try_row][try_col] == 'T':
            mouse_pos = [try_row, try_col]
            print(f"Mouse is trapped!")
            break

        elif matrix[try_row][try_col] == '*':
            mouse_pos = [try_row, try_col]

    else:
        print(f"No more cheese for tonight!")
        break


matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
[print(*x, sep='') for x in matrix]
