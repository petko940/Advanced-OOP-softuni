size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]
spaceship_location = (0, 0)

for i in range(size):
    if 'S' in matrix[i]:
        spaceship_location = (i, matrix[i].index('S'))
        matrix[i][matrix[i].index('S')] = '.'
        break

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

resources = 100
is_lost = False
is_mission_done = False

while True:
    command = input()
    resources -= 5
    new_row = spaceship_location[0] + directions[command][0]
    new_col = spaceship_location[1] + directions[command][1]

    if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:
        is_lost = True
        matrix[spaceship_location[0]][spaceship_location[1]] = 'S'
        break

    if matrix[new_row][new_col] == 'R':
        resources = min(resources + 10, 100)

    elif matrix[new_row][new_col] == 'M':
        resources -= 5
        matrix[new_row][new_col] = '.'
        if resources < 5:
            matrix[new_row][new_col] = 'S'
            break

    elif matrix[new_row][new_col] == 'P':
        is_mission_done = True
        break

    if resources <= 0:
        matrix[new_row][new_col] = 'S'
        break

    spaceship_location = (new_row, new_col)

if is_lost:
    print(f"Mission failed! The spaceship was lost in space.")
elif is_mission_done:
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
else:
    matrix[new_row][new_col] = 'S'
    print(f"Mission failed! The spaceship was stranded in space.")

[print(*x) for x in matrix]
