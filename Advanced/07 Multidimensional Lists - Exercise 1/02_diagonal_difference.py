size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary_diagonal_sum = sum([int(matrix[x][x]) for x in range(len(matrix))])
secondary_diagonal_sum = sum([int(matrix[x][size - 1 - x]) for x in range(len(matrix))])
print(abs(primary_diagonal_sum - secondary_diagonal_sum))
