size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

indexes = [x for x in input().split()]
bombs_indexes = []
for index in indexes:
    row, col = [int(x) for x in index.split(",")]
    bomb = matrix[row][col]

    if bomb > 0:
        if row - 1 >= 0 and col - 1 >= 0:
            if matrix[row - 1][col - 1] > 0:
                matrix[row - 1][col - 1] -= bomb

            if matrix[row - 1][col] > 0:
                matrix[row - 1][col] -= bomb
        if matrix[row][col - 1] > 0:
            matrix[row][col - 1] -= bomb
        if col + 1 < len(matrix[0]):
            if matrix[row - 1][col + 1] > 0:
                matrix[row - 1][col + 1] -= bomb
            if matrix[row][col + 1] > 0:
                matrix[row][col + 1] -= bomb

        matrix[row][col] = 0

        if row + 1 < len(matrix[0]) and col - 1 >= 0:
            if matrix[row + 1][col - 1] > 0:
                matrix[row + 1][col - 1] -= bomb

        if row + 1 < len(matrix[0]) and col + 1 < len(matrix[0]):
            if matrix[row + 1][col] > 0:
                matrix[row + 1][col] -= bomb
            if matrix[row + 1][col + 1] > 0:
                matrix[row + 1][col + 1] -= bomb

count = 0
sum = 0
for mat in matrix:
    for m in mat:
        if m > 0:
            count += 1
            sum += m

print(f"Alive cells: {count}\nSum: {sum}")

for m in matrix:
    print(*m)
