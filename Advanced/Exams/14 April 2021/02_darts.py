def check_bounds(r, c):
    if 0 <= r < 7 and 0 <= c < 7:
        return True
    return False


player_one, player_two = [x for x in input().split(', ')]
matrix = [[x for x in input().split()] for _ in range(7)]

p1, p2, p1_turns, p2_turns = 501, 501, 0, 0
is_player_one = True
while p1 > 0 and p2 > 0:
    command = input()
    row, col = int(command[1:2]), int(command[4:-1])

    if check_bounds(row, col):
        if matrix[row][col].isdigit():
            if is_player_one:
                p1 -= int(matrix[row][col])
            else:
                p2 -= int(matrix[row][col])
        else:
            sum_rows_cols = sum([int(matrix[row][0]), int(matrix[row][-1]), int(matrix[0][col]), int(matrix[-1][col])])
            if matrix[row][col] == 'D':
                if is_player_one:
                    p1 -= sum_rows_cols * 2
                else:
                    p2 -= sum_rows_cols * 2
            elif matrix[row][col] == "T":
                if is_player_one:
                    p1 -= sum_rows_cols * 3
                else:
                    p2 -= sum_rows_cols * 3
            elif matrix[row][col] == "B":
                if is_player_one:
                    p1 = 0
                else:
                    p2 = 0

    if is_player_one:
        p1_turns += 1
        is_player_one = False
    else:
        p2_turns += 1
        is_player_one = True

if p1 <= 0:
    print(f"{player_one} won the game with {p1_turns} throws!")
else:
    print(f"{player_two} won the game with {p2_turns} throws!")
