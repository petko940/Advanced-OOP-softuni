def check_up(b_row, b_col, sum):
    for x in range(b_row - 1, -1, -1):
        if matrix[x][b_col] != "X":
            sum += int(matrix[x][b_col])
            movement["up"].append(f"[{x}, {b_col}]")
        else:
            break
    return sum


def check_down(b_row, b_col, sum):
    for x in range(b_row + 1, size):
        if matrix[x][b_col] != "X":
            sum += int(matrix[x][b_col])
            movement["down"].append(f"[{x}, {b_col}]")
        else:
            break
    return sum


def check_left(b_row, b_col, sum):
    for x in range(b_col - 1, -1, -1):
        if matrix[b_row][x] != "X":
            sum += int(matrix[b_row][x])
            movement["left"].append(f"[{b_row}, {x}]")

        else:
            break
    return sum


def check_right(b_row, b_col, sum):
    for x in range(b_col + 1, size):
        if matrix[b_row][x] != "X":
            sum += int(matrix[b_row][x])
            movement["right"].append(f"[{b_row}, {x}]")
        else:
            break
    return sum


size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0

for i in range(size):
    matrix.append([x for x in input().split()])
    if "B" in matrix[i]:
        bunny_row = i
        bunny_col = matrix[i].index("B")

sum_up, sum_down, sum_left, sum_right = 0, 0, 0, 0
movement = {"up": [], "down": [], "left": [], "right": []}
sum_up = check_up(bunny_row, bunny_col, sum_up)
sum_down = check_down(bunny_row, bunny_col, sum_down)
sum_left = check_left(bunny_row, bunny_col, sum_left)
sum_right = check_right(bunny_row, bunny_col, sum_right)

biggest_sum = {"right": sum_right, "down": sum_down, "left": sum_left, "up": sum_up, }
needed = sorted(biggest_sum.items(), key=lambda x: -x[1])

print(needed[0][0])
for v in movement[needed[0][0]]:
    print(v)
print(needed[0][1])

# result = max(sum_up, sum_down, sum_left, sum_right)
# if sum(biggest_sum.values()) != 0:
#     for k, v in biggest_sum.items():
#         if v == result:
#             print(k)
#             print("\n".join(movement[k]))
#             print(result)
#             break

# needed = sorted(biggest_sum.items(), key=lambda x: -x[1])
# if sum(biggest_sum.values()) != 0:
#     print(needed[0][0])
#     for v in movement[needed[0][0]]:
#         print(v)
#     print(needed[0][1])
