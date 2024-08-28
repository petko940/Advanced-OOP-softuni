n = int(input())

matrix = []

player_pos = [0, 0]

for i in range(n):
    matrix.append([x for x in input().split()])
    if "P" in matrix[i]:
        player_pos[0] = i
        player_pos[1] = matrix[i].index("P")

matrix[player_pos[0]][player_pos[1]] = "."

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_stars = 2
is_game_won = False
while True:
    command = input()

    if player_pos[0] + directions[command][0] < 0 or player_pos[0] + directions[command][0] >= n \
            or player_pos[1] + directions[command][1] < 0 or player_pos[1] + directions[command][1] >= n:
        player_pos[0], player_pos[1] = 0, 0
    else:
        player_pos[0] += directions[command][0]
        player_pos[1] += directions[command][1]

    if matrix[player_pos[0]][player_pos[1]] == "*":
        collected_stars += 1
        matrix[player_pos[0]][player_pos[1]] = "."
        if collected_stars == 10:
            matrix[player_pos[0]][player_pos[1]] = "P"
            is_game_won = True
            break

    elif matrix[player_pos[0]][player_pos[1]] == "#":
        player_pos[0] -= directions[command][0]
        player_pos[1] -= directions[command][1]
        collected_stars -= 1
        if collected_stars == 0:
            matrix[player_pos[0]][player_pos[1]] = "P"
            break

if is_game_won:
    print(f"You won! You have collected 10 stars.")
else:
    print(f"Game over! You are out of any stars.")

print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")
[print(*x, sep=" ") for x in matrix]
