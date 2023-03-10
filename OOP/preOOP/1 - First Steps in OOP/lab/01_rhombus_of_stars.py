n = int(input())

output = []
for row in range(1, n + 1):
    if row == 1:
        output.append(" " * (n - row) + "*" * row)
    else:
        output.append(" " * (n - row) + "* " * row)

for row in range(n - 1, 0, -1):
    if row != 1:
        output.append(" " * (n - row) + "* " * row)
    else:
        output.append(" " * (n - row) + "* " * row)
[print(*x) for x in output]
