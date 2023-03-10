def add(*args):
    col, row, value = [int(x) for x in args]
    if 0 <= col < rows and 0 <= row < rows:
        matrix[col][row] += value
    else:
        print("Invalid coordinates")


def subtract(*args):
    col, row, value = [int(x) for x in args]
    if 0 <= col < rows and 0 <= row < rows:
        matrix[col][row] -= value
    else:
        print("Invalid coordinates")


rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    commands = input()
    if "END" in commands:
        break
    action, row, col, value = [int(x) if x.isdigit() else x for x in commands.split()]
    if action == "Add":
        add(row, col, value)
    elif action == "Subtract":
        subtract(row, col, value)

for row in range(rows):
    print(*matrix[row])
