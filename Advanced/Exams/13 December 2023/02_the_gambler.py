board_size = int(input())

matrix = []

current_row, current_col = 0, 0

for i in range(board_size):
    row = list(input())
    if 'G' in row:
        current_row = i
        current_col = row.index('G')
    matrix.append(row)

matrix[current_row][current_col] = '-'

direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

money = 100


def check_out_of_bounds(r, c):
    if (r < 0 or r >= board_size
            or c < 0 or c >= board_size):
        return True
    return False


def print_jackpot():
    print(f"You win the Jackpot!\n"
          f"End of the game. Total amount: {money}$")
    print_matrix()


def print_bankrupt():
    print("Game over! You lost everything!")
    exit()


def print_matrix():
    [print(*x, sep='') for x in matrix]
    exit()


def print_end_game():
    print(f"End of the game. Total amount: {money}$")
    print_matrix()


while True:
    command = input()
    if command == 'end':
        break

    new_row = current_row + direction[command][0]
    new_col = current_col + direction[command][1]

    if check_out_of_bounds(new_row, new_col):
        print_bankrupt()

    if matrix[new_row][new_col] == 'W':
        money += 100

    elif matrix[new_row][new_col] == 'P':
        money -= 200
        if money <= 0:
            print_bankrupt()

    elif matrix[new_row][new_col] == 'J':
        money += 100000
        matrix[new_row][new_col] = 'G'
        print_jackpot()

    current_row, current_col = new_row, new_col
    matrix[current_row][current_col] = '-'


matrix[current_row][current_col] = 'G'

print_end_game()
