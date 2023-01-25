directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

M = int(input())  # number of presents Santa has
size_matrix = int(input())
matrix = [[x for x in input().split()] for _ in range(size_matrix)]

santa_pos = []
nice_kids, gifted_kids = 0, 0
for i in range(size_matrix):
    if 'S' in matrix[i]:
        santa_pos = [i, matrix[i].index('S')]
        matrix[santa_pos[0]][santa_pos[1]] = '-'
    nice_kids += matrix[i].count('V')


# "X" - naughty kid.
# "V" - nice kid.
# "C" - cookie.

def move(row, col, presents, gifted_kids):  # move
    row += directions[movement][0]
    col += directions[movement][1]
    if matrix[row][col] == 'V':
        presents -= 1
        gifted_kids += 1
        matrix[row][col] = '-'
    elif matrix[row][col] == 'X':
        matrix[row][col] = '-'
    elif matrix[row][col] == "C":
        for direction, value in directions.items():
            r, c = value[0] + row, value[1] + col
            if matrix[r][c] != '-':
                if matrix[r][c] == 'V':
                    gifted_kids += 1
                presents -= 1
                matrix[r][c] = '-'
                if presents == 0:
                    return row, col, presents, gifted_kids
    return row, col, presents, gifted_kids


while True:
    movement = input()
    if movement.startswith('Christmas'):
        break

    santa_pos[0], santa_pos[1], M, gifted_kids = move(santa_pos[0], santa_pos[1], M, gifted_kids)
    if nice_kids == gifted_kids:
        break
    if M == 0 and nice_kids > 0:
        print("Santa ran out of presents!")
        break

matrix[santa_pos[0]][santa_pos[1]] = 'S'
[print(*x) for x in matrix]
if nice_kids == gifted_kids:
    print(f"Good job, Santa! {gifted_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - gifted_kids} nice kid/s.")
