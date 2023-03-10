rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if "swap" not in command[0] or len(command) != 5 \
            or not (command[1].isdigit()
                    or command[2].isdigit()
                    or command[3].isdigit()
                    or command[4].isdigit()):
        print("Invalid input!")
        continue
    com, row1, col1, row2, col2 = [int(x) if x.isdigit() else x for x in command]
    if 0 <= row1 < columns or 0 <= col1 < rows \
            or 0 <= row2 < columns or 0 <= col2 < rows:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for r in range(rows):
            print(*matrix[r])
    else:
        print("Invalid input!")
