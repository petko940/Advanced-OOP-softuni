directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]

bunny_pos = []
for i in range(size):
    if 'B' in matrix[i]:
        bunny_pos = [i, matrix[i].index('B')]
        break

best_direction_sum = 0
best_path, best_steps = None, None

for direction, value in directions.items():
    row = bunny_pos[0] + value[0]
    col = bunny_pos[1] + value[1]
    current_sum = 0
    current_steps = []
    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] != 'X':
            current_sum += int(matrix[row][col])
            current_steps.append(f'[{row}, {col}]')
        else:
            break
        row += value[0]
        col += value[1]
    if current_sum >= best_direction_sum:
        best_direction_sum = current_sum
        best_path = direction
        best_steps = current_steps

print(best_path)
[print(x) for x in best_steps]
print(best_direction_sum)
