# 'P' - starting position of the traveller
# 'X' - exit
# 'M' - monster
# 'H' - health potion
# '-' – empty

n = int(input())
health = 100

position = (0, 0)

matrix = [[x for x in input()] for _ in range(n)]

for r in range(n):
    if 'P' in matrix[r]:
        position = (r, matrix[r].index('P'))
        matrix[r][matrix[r].index('P')] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    new_row = position[0] + directions[command][0]
    new_col = position[1] + directions[command][1]
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        continue

    if matrix[new_row][new_col] == 'M':
        health -= 40
        if health <= 0:
            health = 0
            position = (new_row, new_col)
            break
        matrix[new_row][new_col] = '-'

    elif matrix[new_row][new_col] == 'H':
        health = min(health + 15, 100)
        matrix[new_row][new_col] = '-'

    elif matrix[new_row][new_col] == 'X':
        matrix[new_row][new_col] = '-'
        position = (new_row, new_col)
        break

    position = (new_row, new_col)

matrix[position[0]][position[1]] = 'P'
if health:
    print(f"Player escaped the maze. Danger passed!")
else:
    print(f"Player is dead. Maze over!")

print(f"Player's health: {health} units")

[print(''.join(row)) for row in matrix]
