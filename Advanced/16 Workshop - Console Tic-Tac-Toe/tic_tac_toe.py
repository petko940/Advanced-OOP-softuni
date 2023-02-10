players = []
matrix = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]

player_one = input('Player one enter your name: ')
player_two = input('Player two enter your name: ')

while True:
    symbols = ['X', 'O']
    player_one_symbol = input(f'{player_one} would you like to play "X" or "O" ').upper()
    if player_one_symbol not in symbols:
        print(f'{player_one} select "X" or "O"')
    else:
        symbols.remove(player_one_symbol)
        player_two_symbol = symbols[0]
        break

players = [[player_one, player_one_symbol], [player_two, player_two_symbol]]

print('This is the numeration of the board:')
[print(f'| {" | ".join(i)} |') for i in matrix]

for r in range(3):
    for c in range(3):
        matrix[r][c] = " "

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([matrix[i][i] == player_symbol for i in range(3)])
    second_diagonal_win = all([matrix[i][3 - 1 - i] == player_symbol for i in range(3)])

    row_win = any([all(pos == player_symbol for pos in row) for row in matrix])
    col_win = any([all(matrix[r][c] == player_symbol for r in range(3)) for c in range(3)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(f"{player_name} won!")
        raise SystemExit
    elif len(positions) == 0:
        print("Draw")
        raise SystemExit


while True:
    print(f"{players[0][0]} starts first!")
    while True:
        try:
            selected = int(input(f"{players[0][0]} choose number in {positions}"))
            if selected not in positions:
                print(f"Invalid number")
                continue
            else:
                positions.remove(selected)

        except ValueError:
            print(f"Invalid number")
            continue

        r, c = (selected - 1) // 3, (selected - 1) % 3
        matrix[r][c] = players[0][1]
        [print(f'| {" | ".join(i)} |') for i in matrix]
        check_for_win()
        players[0], players[1] = players[1], players[0]
