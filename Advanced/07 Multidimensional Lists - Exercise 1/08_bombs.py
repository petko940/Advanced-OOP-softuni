directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
    (-1, 1),  # top-right
    (-1, -1),  # top-left
    (1, -1),  # bottom-left
    (1, 1),  # bottom-right
    (0, 0),  # current (this should be last)
)

size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = input()
bombs_coordinates = [x.split(',') for x in bombs.split()]

for row, col in bombs_coordinates:
    row, col = int(row), int(col)
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        x += row
        y += col
        if 0 <= x < size and 0 <= y < size:
            if matrix[x][y] > 0:
                matrix[x][y] -= matrix[row][col]


alive_cells = 0
sum = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")
[print(*x) for x in matrix]
