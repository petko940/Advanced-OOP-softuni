def end_white():
    c = chess["col"][white_col]
    r = chess["row"][white_row]
    print(f"Game over! White pawn is promoted to a queen at {c}{r}.")
    quit()


def white_capture():
    c = chess["col"][column]
    r = chess["row"][row]
    print(f"Game over! White win, capture on {c}{r}.")
    quit()


def end_black():
    c = chess["col"][black_col]
    r = chess["row"][black_row]
    print(f"Game over! Black pawn is promoted to a queen at {c}{r}.")
    quit()


def black_capture():
    c = chess["col"][column]
    r = chess["row"][row]
    print(f"Game over! Black win, capture on {c}{r}.")
    quit()


chess = {
    "row": {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1},
    "col": {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
}

size = 8
matrix = []
for i in range(size):
    matrix.append([x for x in input().split()])

white_row, white_col = 0, 0
black_row, black_col = 0, 0
for i in range(size):
    if "w" in matrix[i]:
        white_row = i
        white_col = matrix[i].index("w")
    if "b" in matrix[i]:
        black_row = i
        black_col = matrix[i].index("b")

row, column = 0, 0
count = 0
check = True
while True:
    if count % 2 == 0:
        if "b" in matrix[white_row]:
            check = False
        if check:
            if white_col - 1 >= 0:
                if matrix[white_row - 1][white_col - 1] == "b":
                    row = white_row - 1
                    column = white_col - 1
                    white_capture()
            if white_col + 1 < 8:
                if matrix[white_row - 1][white_col + 1] == "b":
                    row = white_row - 1
                    column = white_col + 1
                    white_capture()
        if white_row > 0:
            matrix[white_row][white_col] = "-"
            white_row -= 1
            matrix[white_row][white_col] = "w"
            if white_row == 0:
                end_white()
    else:
        if "w" in matrix[black_row]:
            check = False
        if check:
            if black_col - 1 >= 0:
                if matrix[black_row + 1][black_col - 1] == "w":
                    row = black_row + 1
                    column = black_col - 1
                    black_capture()
            if black_col + 1 < 8:
                if matrix[black_row + 1][black_row + 1] == "w":
                    row = black_row + 1
                    column = black_col + 1
                    black_capture()
        if black_row < 7:
            matrix[black_row][black_col] = "-"
            black_row += 1
            matrix[black_row][black_col] = "b"
            if black_row == 7:
                end_black()
    count += 1
