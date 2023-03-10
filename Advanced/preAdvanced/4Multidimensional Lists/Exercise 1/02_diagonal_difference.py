size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []
for row in range(size):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][-row - 1])

primary_diagonal = sum(primary_diagonal)
secondary_diagonal = sum(secondary_diagonal)
difference = abs(primary_diagonal - secondary_diagonal)
print(difference)
