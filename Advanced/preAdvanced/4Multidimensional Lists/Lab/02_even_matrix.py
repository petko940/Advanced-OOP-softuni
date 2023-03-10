rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]

output = [[x for x in row if x % 2 == 0] for row in matrix]

print(output)
