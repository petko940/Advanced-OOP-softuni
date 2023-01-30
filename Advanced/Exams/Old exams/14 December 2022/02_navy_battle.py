size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

pos = []
for i in range(size):
    if 'S' in matrix[i]:
        pos = [i, matrix[i].index('S')]
        matrix[pos[0]][pos[1]] = '-'


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

row, col = pos[0], pos[1]
hits_by_mine = 0
cruisers = 0
while True:  # hits_by_mine < 3 and cruisers > 0:
    command = input()
    row += directions[command][0]
    col += directions[command][1]
    if matrix[row][col] == '*':
        matrix[row][col] = "-"
        hits_by_mine += 1
        if hits_by_mine == 3:
            matrix[row][col] = 'S'
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
            break
    elif matrix[row][col] == 'C':
        matrix[row][col] = "-"
        cruisers += 1
        if cruisers == 3:
            matrix[row][col] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

[print(*x, sep='') for x in matrix]
