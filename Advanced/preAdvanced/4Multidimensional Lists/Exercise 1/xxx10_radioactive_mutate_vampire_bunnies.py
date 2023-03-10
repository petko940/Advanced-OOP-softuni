def bunny():
    print(matrix)
    for i in range(rows):
        if "B" in matrix[i]:
            for x in matrix[i]:
                b_row = i
                b_col = matrix[i].index("B")
                if 0 < b_row - 1:
                    matrix[b_row - 1][b_col] = "B"
                if b_row + 1 < rows:
                    matrix[b_row + 1][b_col] = "B"
                if 0 < b_col - 1:
                    matrix[b_row][b_col - 1] = "B"
                if b_col + 1 < columns:
                    matrix[b_row][b_col + 1] = "B"
                break
            break
    for x in matrix:
        print(x)

def up():
    matrix[player_row_index][player_column_index] = "."
    matrix[player_row_index - 1][player_column_index] = "P"



def down():
    pass


def left():
    pass


def right():
    pass


def win(*args):
    up()
    bunny()

    print("won:", *args)


rows, columns = [int(x) for x in input().split()]
matrix = []
player_row_index, player_column_index = 0, 0
for i in range(rows):
    matrix.append([x for x in input()])
    if "P" in matrix[i]:
        for x in matrix[i]:
            player_row_index = i
            player_column_index = matrix[i].index("P")
            break

commands = input()
for char in commands:
    if char == "U":
        if 0 < player_row_index:
            up()
        else:
            player_row_index -= 1
            win(player_row_index, player_column_index)
            break
        player_row_index -= 1
    elif char == "D":
        if rows >= player_row_index:
            down()
        else:
            win(player_row_index, player_column_index)
            break
        player_row_index += 1
    elif char == "L":
        left()
    elif char == "R":
        right()
