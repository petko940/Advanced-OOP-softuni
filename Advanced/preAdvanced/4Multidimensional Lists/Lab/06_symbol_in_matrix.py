n = int(input())

matrix = [input() for x in range(n)]
symbol = input()

for row in range(n):
    if symbol in matrix[row]:
        print(f"({row}, ", end="")
        col = matrix[row].index(symbol)
        print(f"{col})")
        break
else:
    print(f"{symbol} does not occur in the matrix")
