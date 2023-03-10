rows, columns = [int(x) for x in input().split(", ")]

# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
matrix = []
for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

sum_numbers = 0
for x in matrix:
    sum_numbers += sum(x)
print(sum_numbers)

print(matrix)
