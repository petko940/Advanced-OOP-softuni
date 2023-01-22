movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

snake_row, snake_col = 0, 0
burrows_pos = []
for i in range(size):
    if "S" in matrix[i]:
        snake_row = i
        snake_col = matrix[i].index("S")

    if "B" in matrix[i]:
        burrows_pos.append((i, matrix[i].index("B")))


def check_position(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


eaten_food = 0
is_done = False
while eaten_food < 10:
    command = input()
    if check_position(snake_row + movement[command][0], snake_col + movement[command][1]):
        matrix[snake_row][snake_col] = "."
        snake_row += movement[command][0]
        snake_col += movement[command][1]
        if matrix[snake_row][snake_col] == "*":
            eaten_food += 1
            matrix[snake_row][snake_col] = "S"
            if eaten_food == 10:
                is_done = True
        elif matrix[snake_row][snake_col] == "B":
            if burrows_pos[0] == (snake_row, snake_col):
                matrix[snake_row][snake_col] = "."
                snake_row = burrows_pos[1][0]
                snake_col = burrows_pos[1][1]
            else:
                matrix[snake_row][snake_col] = "."
                snake_row = burrows_pos[0][0]
                snake_col = burrows_pos[0][1]
    else:
        matrix[snake_row][snake_col] = "."
        print("Game over!")
        break

if is_done:
    print("You won! You fed the snake.")

print(f"Food eaten: {eaten_food}")
[print(*x, sep="") for x in matrix]
