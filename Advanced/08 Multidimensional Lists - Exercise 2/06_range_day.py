directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
matrix = [[x for x in input().split()] for _ in range(5)]

player_pos = []
count_targets = 0
hit_target = []

for i in range(5):
    if 'A' in matrix[i]:
        player_pos.append(i)
        player_pos.append(matrix[i].index('A'))
        matrix[player_pos[0]][player_pos[1]] = '.'
    count_targets += matrix[i].count('x')


def move(direction, steps):
    row = player_pos[0] + directions[direction][0] * steps
    col = player_pos[1] + directions[direction][1] * steps
    if 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] != 'x':
        player_pos[0] = row
        player_pos[1] = col
    return player_pos


def shoot(direction, row, col):
    x = row + directions[direction][0]
    y = col + directions[direction][1]
    while True:
        if 0 <= x < 5 and 0 <= y < 5 and matrix[x][y] != 'x':
            x += directions[direction][0]
            y += directions[direction][1]
        if 0 <= x < 5 and 0 <= y < 5 and matrix[x][y] == 'x':
            hit_target.append(f'[{x}, {y}]')
            matrix[x][y] = '.'
            break
        if not (0 <= x < 5 and 0 <= y < 5):
            break


for _ in range(int(input())):
    command = input()
    if command.startswith('move'):
        event, direction, steps = [int(x) if x.isdigit() else x for x in command.split()]
        move(direction, steps)
    elif command.startswith('shoot'):
        event, direction = command.split()
        shoot(direction, player_pos[0], player_pos[1])
        if count_targets == len(hit_target):
            break

if count_targets == len(hit_target):
    print(f"Training completed! All {count_targets} targets hit.")
else:
    print(f"Training not completed! {count_targets - len(hit_target)} targets left.")
[print(x) for x in hit_target]
