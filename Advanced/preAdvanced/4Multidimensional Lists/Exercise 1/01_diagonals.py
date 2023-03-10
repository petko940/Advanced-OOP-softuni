n = int(input())

matrix = []
for row in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary_diagonal = []
secondary_diagonal = []

primary_index = 0
sec_index = -1
col = 0
for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][sec_index])
    primary_index += 1
    sec_index -= 1
    col += 1

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
