size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]

# sum_primary_diagonal = 0
# for i in range(size):
#     sum_primary_diagonal += matrix[i][i]

sum_primary_diagonal = [int(matrix[x][x]) for x in range(size)]
print(sum(sum_primary_diagonal))
