text = input()
size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

player_pos = []
for i in range(size):
    if "P" in matrix[i]:
        player_pos = [i, matrix[i].index("P")]
        matrix[i][player_pos[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def check_bound(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


for _ in range(int(input())):
    command = input()
    if check_bound(player_pos[0] + directions[command][0],
                   player_pos[1] + directions[command][1]):
        player_pos[0] += directions[command][0]
        player_pos[1] += directions[command][1]
        if matrix[player_pos[0]][player_pos[1]] != '-':
            text += matrix[player_pos[0]][player_pos[1]]
            matrix[player_pos[0]][player_pos[1]] = '-'
    else:
        text = text[:-1]

matrix[player_pos[0]][player_pos[1]] = 'P'
print(text)
[print(*x, sep='') for x in matrix]
