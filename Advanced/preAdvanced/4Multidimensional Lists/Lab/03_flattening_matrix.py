rows = int(input())

matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

output = []
for row in range(rows):
    for r in matrix[row]:
        output.append(r)

print(output)
