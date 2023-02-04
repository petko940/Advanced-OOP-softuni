def player_turn(number):
    while True:
        turn = int(input(f'Player {number}, please choose a column:\n'))
        if turn < 1:
            print("Enter number between 1 and 7")
            continue
        else:
            break
    return turn


def check_bounds(row, col):
    if 0 <= row < 6 and 0 <= col < 7:
        return True
    return False


def game_over():
    print(f"The winner is player {player_one}")
    quit()


matrix = [[0 for x in range(7)] for _ in range(6)]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

player_one, player_two = 1, 2
while True:
    col = player_turn(player_one) - 1
    row = 0

    try:
        while row < len(matrix) - 1 and matrix[row][col] == 0:
            if matrix[row + 1][col] != 0:
                matrix[row][col] = player_one
                break
            row += 1
        else:
            if row != 0:
                matrix[row][col] = player_one
    except IndexError:
        print("Enter number between 1 and 7")
        continue

    for r, c in directions:
        count_to_win = 0
        test_row = row
        test_col = col
        for _ in range(4):
            if check_bounds(test_row + r, test_col + c):
                test_row += r
                test_col += c
                if matrix[test_row][test_col] == player_one:
                    count_to_win += 1
                    if count_to_win == 3:
                        game_over()
                else:
                    break

    player_one, player_two = player_two, player_one
    [print(x) for x in matrix]
