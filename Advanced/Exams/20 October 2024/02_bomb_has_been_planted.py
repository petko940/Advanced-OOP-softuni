rows, cols = [int(x) for x in input().split(', ')]

matrix = []

seconds_remaining = 16
counter_terrorist_pos = None
for r in range(rows):
    row = input()
    matrix.append([x for x in row])
    if 'C' in matrix[r]:
        counter_terrorist_pos = (r, matrix[r].index('C'))

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

is_bomb_defused = False
is_bomb_defusing = False
is_counter_terrorist_killed = False
while True:
    command = input()
    row, col = counter_terrorist_pos[0], counter_terrorist_pos[1]

    if 'defuse' in command:
        if matrix[row][col] != 'B':
            seconds_remaining -= 2
            if seconds_remaining <= 0:
                break
            continue
        else:
            is_bomb_defusing = True
            seconds_remaining -= 4
            if seconds_remaining >= 0:
                matrix[row][col] = 'D'
                is_bomb_defused = True
            else:
                matrix[row][col] = 'X'
            break

    new_row, new_col = row + movements[command][0], col + movements[command][1]

    if (new_row < 0 or new_row >= rows or
            new_col < 0 or new_col >= cols):
        seconds_remaining -= 1
        continue

    if matrix[new_row][new_col] == 'T':
        is_counter_terrorist_killed = True
        matrix[new_row][new_col] = '*'
        break

    counter_terrorist_pos = (new_row, new_col)

    seconds_remaining -= 1
    if seconds_remaining <= 0:
        break

if is_counter_terrorist_killed:
    print("Terrorists win!")
elif not is_bomb_defused and not is_counter_terrorist_killed:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(seconds_remaining) if is_bomb_defusing else 0} second/s.")
elif is_bomb_defused and not is_counter_terrorist_killed:
    print(f"Counter-terrorist wins!")
    print(f"Bomb has been defused: {seconds_remaining} second/s remaining.")

[print(*x, sep='') for x in matrix]
