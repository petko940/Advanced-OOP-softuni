"""
    • 'B' - Represents the starting position of the delivery boy.
    • 'A' - Represents an address where a pizza needs to be delivered.
    • '*' - Represents an obstacle or an area where the delivery boy cannot drive.
    • 'P' - Represents the pizza restaurant.
    • '-' – Represents the road, the delivery boy can drive over it.
"""

moving = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

rows, columns = [int(x) for x in input().split()]

matrix = []
start_pos = []

for r in range(rows):
    matrix.append([x for x in input()])
    if 'B' in matrix[r]:
        start_pos = [r, matrix[r].index('B')]

pos_x, pos_y = start_pos[0], start_pos[1]
while True:
    command = input()

    if (not 0 <= moving[command][0] + pos_x < rows) or (not 0 <= moving[command][1] + pos_y < columns):
        matrix[start_pos[0]][start_pos[1]] = " "
        print(f"The delivery is late. Order is canceled.")
        break

    if matrix[moving[command][0] + pos_x][moving[command][1] + pos_y] == '*':
        continue

    pos_x += moving[command][0]
    pos_y += moving[command][1]

    if matrix[pos_x][pos_y] == 'P':
        matrix[pos_x][pos_y] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue

    elif matrix[pos_x][pos_y] == 'A':
        matrix[pos_x][pos_y] = 'P'
        print(f"Pizza is delivered on time! Next order...")
        break

    elif matrix[pos_x][pos_y] == '-':
        matrix[pos_x][pos_y] = '.'

[print(''.join(x)) for x in matrix]
