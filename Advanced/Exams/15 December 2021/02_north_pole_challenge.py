"""  • Your position is marked with the symbol "Y"
    • Christmas decorations are marked with the symbol "D"
    • Gifts are marked with the symbol "G"
    • Cookies are marked with the symbol "C"
    • All of the empty positions will be marked with "."
"""
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

rows, columns = [int(x) for x in input().split(', ')]
matrix = [[x for x in input().split()] for _ in range(rows)]

christmas_decorations, gifts, cookies = 0, 0, 0
total_items = 0
my_row, my_col = 0, 0
for x in range(rows):
    if 'Y' in matrix[x]:
        my_row, my_col = x, matrix[x].index('Y')
    total_items += matrix[x].count('D')
    total_items += matrix[x].count('G')
    total_items += matrix[x].count('C')


def move(row, col, christmas_decoration, gift, cookie):
    matrix[row][col] = 'x'
    for x in range(steps):
        row += moves[direction][0]
        col += moves[direction][1]
        if row < 0:
            row = rows - 1
        elif row >= rows:
            row = 0
        if col < 0:
            col = columns - 1
        elif col >= columns:
            col = 0

        if matrix[row][col] == 'D':
            christmas_decoration += 1
        elif matrix[row][col] == 'G':
            gift += 1
        elif matrix[row][col] == 'C':
            cookie += 1
        if christmas_decoration + gift + cookie == total_items:
            break
        matrix[row][col] = 'x'
    matrix[row][col] = 'Y'
    return row, col, christmas_decoration, gift, cookie


while True:
    commands = input()
    if commands == "End":
        break
    direction, steps = [int(x) if x.isdigit() else x for x in commands.split('-')]
    my_row, my_col, christmas_decorations, gifts, cookies = \
        move(my_row, my_col, christmas_decorations, gifts, cookies)
    if christmas_decorations + gifts + cookies == total_items:
        print("Merry Christmas!")
        break

print(f"""You've collected:
- {christmas_decorations} Christmas decorations
- {gifts} Gifts
- {cookies} Cookies""")
[print(*x) for x in matrix]
