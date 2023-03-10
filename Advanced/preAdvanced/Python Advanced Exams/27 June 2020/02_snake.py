size = int(input())
matrix = [[x for x in input()] for x in range(size)]
movement = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}

eaten_enough = 0
snake_row, snake_col = 0, 0
burrows = []
for index, value in enumerate(matrix):
    if "S" in matrix[index]:
        snake_row = index
        snake_col = matrix[index].index("S")
    if "B" in matrix[index]:
        burrows.append(index)
        burrows.append(matrix[index].index("B"))


def move(row, col, eaten):
    matrix[row][col] = "."
    row += movement[command]["row"]
    col += movement[command]["col"]
    if row < 0 or row >= size or col < 0 or col >= size:
        end(eaten)
    if matrix[row][col] == "*":
        eaten += 1
    elif matrix[row][col] == "B":
        if row == burrows[0] and col == burrows[1]:
            matrix[row][col] = "."
            row, col = burrows[2], burrows[3]
        else:
            matrix[row][col] = "."
            row, col = one_burrow_row, one_burrow_col
    matrix[row][col] = "S"
    return row, col, eaten


def end(eaten):
    print("Game over!")
    print(f"Food eaten: {eaten}")
    [print(*x, sep="") for x in matrix]
    quit()


while eaten_enough != 10:
    command = input()
    snake_row, snake_col, eaten_enough = move(snake_row, snake_col, eaten_enough)

print(f"""You won! You fed the snake.
Food eaten: {eaten_enough}""")
[print(*x, sep="") for x in matrix]
