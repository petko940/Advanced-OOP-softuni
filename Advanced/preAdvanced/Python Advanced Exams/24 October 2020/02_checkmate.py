size = 8
matrix = [[x for x in input().split()] for x in range(size)]
# [print(*x) for x in matrix]

queens_positions = []
for i in range(size):
    if "Q" in matrix[i]:
        for index, item in enumerate(matrix[i]):
            if item == "Q":
                queens_positions.append((i, index))

checkmates = []
for current_queen in queens_positions:
    row = current_queen[0]
    col = current_queen[1]
    # horizontal
    for c in range(col + 1, size):
        if matrix[row][c] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[row][c] == "Q":
            break
    for c in range(col - 1, -1, -1):
        if matrix[row][c] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[row][c] == "Q":
            break
    # vertical
    for r in range(row + 1, size):
        if matrix[r][col] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[r][col] == "Q":
            break
    for r in range(row - 1, -1, -1):
        if matrix[r][col] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[r][col] == "Q":
            break
    # diagonal
    right_down = col + 1
    for d in range(row + 1, size):
        if right_down > 7:
            break
        if matrix[d][right_down] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[d][right_down] == "Q":
            break
        right_down += 1
        if right_down > 7:
            break
    left_up = row - 1
    for z in range(col - 1, -1, -1):
        if left_up < 0:
            break
        if matrix[left_up][z] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[left_up][z] == "Q":
            break
        left_up -= 1
        if left_up < 0:
            break
    right_up = col + 1
    for h in range(row - 1, -1, -1):
        if right_up > 7:
            break
        if matrix[h][right_up] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[h][right_up] == "Q":
            break
        right_up += 1
        if right_up > 7:
            break
    left_down = row + 1
    for v in range(col - 1, -1, -1):
        if left_down > 7:
            break
        if matrix[left_down][v] == "K":
            checkmates.append(f"[{row}, {col}]")
            break
        elif matrix[left_down][v] == "Q":
            break
        left_down += 1
        if left_down > 7:
            break

if checkmates:
    [print(x) for x in checkmates]
else:
    print("The king is safe!")