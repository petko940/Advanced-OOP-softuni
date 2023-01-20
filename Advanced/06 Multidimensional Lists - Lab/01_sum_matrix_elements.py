rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

sum_numbers = 0
for i in matrix:
    sum_numbers += sum(i)

print(sum_numbers)
print(matrix)
