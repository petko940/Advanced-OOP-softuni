positions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


def moving(row, col, presents, nice_kids):
    matrix[row][col] = "-"
    row += positions[command][0]
    col += positions[command][1]
    if matrix[row][col] == "X":
        pass
    if matrix[row][col] == "V":
        presents -= 1
        nice_kids -= 1
    if matrix[row][col] == "C":
        # up
        if row - 1 >= 0:
            if matrix[row - 1][col] == "V":
                presents -= 1
                nice_kids -= 1
            elif matrix[row - 1][col] == "X":
                presents -= 1
            matrix[row - 1][col] = "-"
        # down
        if row + 1 < size:
            if matrix[row + 1][col] == "V":
                presents -= 1
                nice_kids -= 1
            elif matrix[row + 1][col] == "X":
                presents -= 1
            matrix[row + 1][col] = "-"

        # left
        if col - 1 >= 0:
            if matrix[row][col - 1] == "V":
                presents -= 1
                nice_kids -= 1
            elif matrix[row][col - 1] == "X":
                presents -= 1
            matrix[row][col - 1] = "-"
        # right
        if col + 1 < size:
            if matrix[row][col + 1] == "V":
                presents -= 1
                nice_kids -= 1
            elif matrix[row][col + 1] == "X":
                presents -= 1
            matrix[row][col + 1] = "-"
    matrix[row][col] = "S"
    return row, col, presents, nice_kids


"""
santa - S
naughty kid - X
nice kid - V
cookies - C
empty positions - "-"
"""
presents = int(input())
size = int(input())
matrix = [[x for x in input().split()] for x in range(size)]

count_nice_kids = 0

santa_row, santa_col = 0, 0
for index in range(size):
    if "S" in matrix[index]:
        santa_row = index
        santa_col = matrix[index].index("S")
    if "V" in matrix[index]:
        for i, kid in enumerate(matrix[index]):
            if kid == "V":
                count_nice_kids += 1

started_kids = count_nice_kids

while True:
    can_i_move = False
    command = input()
    if command == 'Christmas morning':
        break
    if command == "up" and santa_row - 1 >= 0:
        can_i_move = True
    elif command == "down" and santa_row + 1 < size:
        can_i_move = True
    elif command == "left" and santa_col - 1 >= 0:
        can_i_move = True
    elif command == "right" and santa_col + 1 < size:
        can_i_move = True
    if can_i_move:
        santa_row, santa_col, presents, count_nice_kids = moving(santa_row, santa_col, presents, count_nice_kids)
    if presents <= 0 < count_nice_kids:
        print("Santa ran out of presents!")
        break

for i in matrix:
    print(*i)

if count_nice_kids > 0:
    print(f"No presents for {count_nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {started_kids} happy nice kid/s.")
