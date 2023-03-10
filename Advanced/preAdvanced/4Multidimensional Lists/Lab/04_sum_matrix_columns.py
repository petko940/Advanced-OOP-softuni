rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for x in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    sum_colum = 0
    for row in range(rows):
        sum_colum += matrix[row][col]
    print(sum_colum)
