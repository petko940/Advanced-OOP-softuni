rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

biggest_sum = 0
matrix_output = [[], []]
for row in range(rows - 1):
    for col in range(columns - 1):
        current_sum = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        if sum(current_sum) > biggest_sum:
            biggest_sum = sum(current_sum)
            matrix_output = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

[print(*x) for x in matrix_output]
print(biggest_sum)
