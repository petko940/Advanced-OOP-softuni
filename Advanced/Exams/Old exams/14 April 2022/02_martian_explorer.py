matrix = [[x for x in input().split()] for _ in range(6)]

pos = []
for i in range(6):
    if 'E' in matrix[i]:
        pos = [i, matrix[i].index('E')]
        matrix[i][pos[1]] = "-"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def check_bounds(row, col):
    if 0 > row:
        row = 5
    elif row >= 6:
        row = 0
    if 0 > col:
        col = 5
    elif col >= 6:
        col = 0
    return row, col


water, metal, concrete = 0, 0, 0
commands = input().split(', ')
for command in commands:
    pos[0] += directions[command][0]
    pos[1] += directions[command][1]
    pos[0], pos[1] = check_bounds(pos[0], pos[1])
    if matrix[pos[0]][pos[1]] == "W":
        water += 1
        print(f"Water deposit found at ({pos[0]}, {pos[1]})")
    elif matrix[pos[0]][pos[1]] == "M":
        metal += 1
        print(f"Metal deposit found at ({pos[0]}, {pos[1]})")
    elif matrix[pos[0]][pos[1]] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({pos[0]}, {pos[1]})")
    elif matrix[pos[0]][pos[1]] == "R":
        print(f"Rover got broken at ({pos[0]}, {pos[1]})")
        break

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
