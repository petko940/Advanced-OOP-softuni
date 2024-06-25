size = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []

bee_position = []

for r in range(size):
    row = input()
    if 'B' in row:
        bee_position = [r, row.index('B')]

    matrix.append([x for x in row])

matrix[bee_position[0]][bee_position[1]] = '-'

energy, collected = 15, 0  # required to be collected 30
energy_restored = False

while True:
    command = input()
    new_row = bee_position[0] + directions[command][0]
    new_col = bee_position[1] + directions[command][1]

    if new_row < 0:
        new_row = size - 1
    elif new_row > size - 1:
        new_row = 0
    if new_col < 0:
        new_col = size - 1
    elif new_col > size - 1:
        new_col = 0

    energy -= 1

    if matrix[new_row][new_col].isdigit():
        collected += int(matrix[new_row][new_col])

    elif matrix[new_row][new_col] == 'H':
        if collected >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if energy == 0:
        if collected < 30:
            print("This is the end! Beesy ran out of energy.")
            break
        elif not energy_restored and collected >= 30:
            energy += (collected - 30)
            collected = 30
            energy_restored = True

    if energy == 0 and energy_restored:
        print("This is the end! Beesy ran out of energy.")
        break

    matrix[new_row][new_col] = '-'
    bee_position = [new_row, new_col]

matrix[new_row][new_col] = 'B'
[print(''.join(x)) for x in matrix]
