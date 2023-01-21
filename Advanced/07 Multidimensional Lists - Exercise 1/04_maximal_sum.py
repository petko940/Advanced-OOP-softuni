rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

best_matrix = []
best_matrix_sum = -1000

for row in range(rows - 2):
    for col in range(columns - 2):
        row1 = matrix[row][col: col + 3]
        row2 = matrix[row + 1][col: col + 3]
        row3 = matrix[row + 2][col: col + 3]
        if sum(row1 + row2 + row3) > best_matrix_sum:
            best_matrix_sum = sum(row1 + row2 + row3)
            best_matrix = [row1, row2, row3]

print(f"Sum = {best_matrix_sum}")
([print(*x) for x in best_matrix])
