"""
    • One player - randomly placed in it and marked with the symbol "P"
    • Numbers for coins placed at different positions of the field
    • Walls marked with "X"
"""
movement = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}
size = int(input())
matrix = [[x for x in input().split()] for x in range(size)]
row, col = 0, 0
for i in range(size):
    if "P" in matrix[i]:
        row = i
        col = matrix[i].index("P")


def move(current_row, current_col, coins, end_game):
    current_row += movement[command]["row"]
    current_col += movement[command]["col"]
    if current_row < 0:
        current_row = size - 1
    elif current_row >= size:
        current_row = 0
    elif current_col < 0:
        current_col = size - 1
    elif current_col >= size:
        current_col = 0
    output_positions.append(f"[{current_row}, {current_col}]")
    if matrix[current_row][current_col].isdigit():
        coins += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = "0"
    elif matrix[current_row][current_col] == "X":
        end_game = True
    return current_row, current_col, coins, end_game


output_positions = []
collected_coins = 0
end_game = False
output_positions.append(f"[{row}, {col}]")
while collected_coins < 100:
    command = input()
    row, col, collected_coins, end_game = move(row, col, collected_coins, end_game)
    if end_game:
        collected_coins //= 2
        print(f"Game over! You've collected {collected_coins} coins.")
        break
else:
    print(f"You won! You've collected {collected_coins} coins.")

print("Your path:")
[print(x) for x in output_positions]
