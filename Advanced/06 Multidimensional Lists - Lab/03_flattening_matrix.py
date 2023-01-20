rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for y in range(rows)]

output = []
for row in matrix:
    for el in row:
        output.append(el)

print(output)
