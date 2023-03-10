n = int(input())

matrix = []
for x in range(n):
    matrix.append([int(x) for x in input().split()])

result = []
for col in range(1):
    for row in range(n):
        result.append(matrix[row][col])
        col += 1
        continue

print(sum(result))
