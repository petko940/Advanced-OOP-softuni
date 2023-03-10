rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

total_sum = -400
matrix_3x3 = []
for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = 0
        # current_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
        #                   matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
        #                   matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        row1 = matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
        row2 = matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
        row3 = matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        current_matrix = [row1, row2, row3]
        for numbers in current_matrix:
            for num in numbers:
                current_sum += num
        if current_sum > total_sum:
            total_sum = current_sum
            matrix_3x3 = current_matrix

print(f"Sum = {total_sum}")

for x in range(3):
    for y in range(3):
        print(matrix_3x3[x][y], end=" ")
    print()
