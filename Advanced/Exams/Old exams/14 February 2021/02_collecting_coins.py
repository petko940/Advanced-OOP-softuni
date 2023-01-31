directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]

pos = []
for i in range(size):
    if "P" in matrix[i]:
        pos = [i, matrix[i].index('P')]
        matrix[i][pos[1]] = "0"


def check_bounds(row, col):
    if 0 > row:
        row = size - 1
    elif row >= size:
        row = 0
    if 0 > col:
        col = size - 1
    elif col >= size:
        col = 0
    return row, col


coins = 0
path = [f"[{pos[0]}, {pos[1]}]"]
while coins < 100:
    command = input()
    pos[0] += directions[command][0]
    pos[1] += directions[command][1]
    pos[0], pos[1] = check_bounds(pos[0], pos[1])
    path.append(f'[{pos[0]}, {pos[1]}]')
    if matrix[pos[0]][pos[1]].isdigit():
        coins += int(matrix[pos[0]][pos[1]])
        matrix[pos[0]][pos[1]] = "0"
    else:
        break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    coins //= 2
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
[print(*x, sep="") for x in path]
