"""
    • Your position is marked with the symbol "Y"
    • Christmas decorations are marked with the symbol "D"
    • Gifts are marked with the symbol "G"
    • Cookies are marked with the symbol "C"
    • All of the empty positions will be marked with "."
"""
position = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}

rows, columns = [int(x) for x in input().split(", ")]
matrix = [[x for x in input().split()] for x in range(rows)]
row, col = 0, 0
d_count, g_count, c_count = 0, 0, 0
for i, item in enumerate(range(rows)):
    if "Y" in matrix[i]:
        row = i
        col = matrix[i].index("Y")
    if "D" in matrix[i]:
        for x in matrix[i]:
            if x == "D":
                d_count += 1
    if "G" in matrix[i]:
        for x in matrix[i]:
            if x == "G":
                g_count += 1
    if "C" in matrix[i]:
        for x in matrix[i]:
            if x == "C":
                c_count += 1


def movement(f_row, f_col, step, chr_count, gifts_count, cookies_count, d_count, g_count, c_count, ):
    matrix[f_row][f_col] = "x"
    for x in range(step):
        f_row += position[direction]["row"]
        if f_row < 0:
            f_row = rows - 1
        if f_row > rows - 1:
            f_row = 0
        f_col += position[direction]["col"]
        if f_col < 0:
            f_col = columns - 1
        if f_col > columns - 1:
            f_col = 0

        if matrix[f_row][f_col] == "D":
            chr_count += 1
        elif matrix[f_row][f_col] == "G":
            gifts_count += 1
        elif matrix[f_row][f_col] == "C":
            cookies_count += 1

        if d_count + g_count + c_count == chr_count + gifts_count + cookies_count:
            break
        matrix[f_row][f_col] = "x"
    matrix[f_row][f_col] = "Y"
    return f_row, f_col, chr_count, gifts_count, cookies_count


chr_count, gifts_count, cookies_count = 0, 0, 0
while True:
    commands = input()
    if commands == "End":
        break
    direction, steps = [int(x) if x.isdigit() else x for x in commands.split("-")]
    row, col, chr_count, gifts_count, cookies_count = movement(row, col, steps, chr_count, gifts_count, cookies_count,
                                                               d_count, g_count, c_count)
    if d_count + g_count + c_count == chr_count + gifts_count + cookies_count:
        print("Merry Christmas!")
        break

print(f"""You've collected:
- {chr_count} Christmas decorations
- {gifts_count} Gifts
- {cookies_count} Cookies""")
[print(*x) for x in matrix]
