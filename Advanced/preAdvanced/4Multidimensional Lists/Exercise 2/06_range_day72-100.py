def check_row(row):
    if 0 > row:
        row = 0
    elif row >= size:
        row = size - 1
    return row


def check_column(col):
    if 0 > col:
        col = 0
    elif col >= size:
        col = size - 1
    return col


def move(*args):
    row, col, arrow, steps = args[0], args[1], args[2], args[3]
    if arrow == "up":
        row -= steps
        row = check_row(row)
    elif arrow == "down":
        row += steps
        row = check_row(row)
    elif arrow == "left":
        col -= steps
        col = check_column(col)
    elif arrow == "right":
        col += steps
        col = check_column(col)
    return row, col


def shoot(direction, row, col, marks_count):
    if direction == "up":
        row -= 1
        while True:
            if row < 0:
                break
            if matrix[row][col] == ".":
                row -= 1
            elif matrix[row][col] == "x":
                matrix[row][col] = "."
                hit_marks.append(f"[{row}, {col}]")
                marks_count -= 1
                break
    elif direction == "down":
        row += 1
        while True:
            if row >= size:
                break
            if matrix[row][col] == ".":
                row += 1
            elif matrix[row][col] == "x":
                matrix[row][col] = "."
                hit_marks.append(f"[{row}, {col}]")
                marks_count -= 1
                break
    elif direction == "left":
        col -= 1
        while True:
            if col < 0:
                break
            if matrix[row][col] == ".":
                col -= 1
            elif matrix[row][col] == "x":
                matrix[row][col] = "."
                hit_marks.append(f"[{row}, {col}]")
                marks_count -= 1
                break
    elif direction == "right":
        col += 1
        while True:
            if col >= size:
                break
            if matrix[row][col] == ".":
                col += 1
            elif matrix[row][col] == "x":
                matrix[row][col] = "."
                hit_marks.append(f"[{row}, {col}]")
                marks_count -= 1
                break
    return marks_count


size = 5
matrix = []
my_row, my_col = 0, 0
marks_count = 0
for i in range(size):
    matrix.append([x for x in input().split()])
    if "A" in matrix[i]:
        my_row = i
        my_col = matrix[i].index("A")
    if "x" in matrix[i]:
        for index, item in enumerate(matrix[i]):
            if item == "x":
                marks_count += 1

hit_marks = []
n = int(input())
for _ in range(n):
    command = input().split()
    if "shoot" in command:
        direction = command[1]
        marks_count = shoot(direction, my_row, my_col, marks_count)
    elif "move" in command:
        direction, steps = command[1], int(command[2])
        my_row, my_col = move(my_row, my_col, direction, steps)

    if marks_count == 0:
        print(f"Training completed! All {len(hit_marks)} targets hit.")
        break
else:
    print(f"Training not completed! {marks_count} targets left.")

for mark in hit_marks:
    print(mark)
