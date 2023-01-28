rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]
directions = input()

movements = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

player_pos = []
bunny_pos = []
bunny_pos_copy = []
for m in range(rows):
    if 'P' in matrix[m]:
        player_pos = [m, matrix[m].index('P')]
        matrix[player_pos[0]][player_pos[1]] = "."
    if 'B' in matrix[m]:
        for i in range(columns):
            if matrix[m][i] == "B":
                bunny_pos.append((m, i))


def check_bounds(row, col):
    if 0 <= row < rows and 0 <= col < columns:
        return True
    return False


def fill_with_bunnies():
    for bunny in bunny_pos:
        bunny_pos_copy.append((bunny[0], bunny[1]))
        for v in movements.values():
            if check_bounds(bunny[0] + v[0], bunny[1] + v[1]):
                bunny_pos_copy.append((bunny[0] + v[0], bunny[1] + v[1]))

    bunny_pos.clear()
    bunny_pos.extend(bunny_pos_copy)
    bunny_pos_copy.clear()
    return player_pos[0], player_pos[1]


is_player_on_bunny = False
for d in directions:
    if check_bounds(player_pos[0] + movements[d][0], player_pos[1] + movements[d][1]):
        player_pos[0] += movements[d][0]
        player_pos[1] += movements[d][1]
        fill_with_bunnies()
        if (player_pos[0], player_pos[1]) in bunny_pos:
            is_player_on_bunny = True
            break
    else:
        fill_with_bunnies()
        break

for x in bunny_pos:
    matrix[x[0]][x[1]] = 'B'
[print(*x, sep="") for x in matrix]

if is_player_on_bunny:
    print(f"dead: {player_pos[0]} {player_pos[1]}")
else:
    print(f"won: {player_pos[0]} {player_pos[1]}")
