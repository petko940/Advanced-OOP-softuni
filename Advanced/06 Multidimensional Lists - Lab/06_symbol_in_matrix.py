size = int(input())
matrix = [[x for x in input()] for x in range(size)]

symbol = input()

output = []
for i in range(size):
    if symbol in matrix[i]:
        column = matrix[i].index(symbol)
        output.append(f"({i}, {column})")
        break

if output:
    print(*output)
else:
    print(f"{symbol} does not occur in the matrix")
