rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = 0

max_matrix = []
for col in range(columns - 1):
    for row in range(rows - 1):
        current_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        if sum(current_matrix) > max_sum:
            max_sum = sum(current_matrix)
            max_matrix.clear()
            max_matrix = current_matrix

print(max_matrix[0], max_matrix[1])
print(max_matrix[2], max_matrix[3])
print(max_sum)
