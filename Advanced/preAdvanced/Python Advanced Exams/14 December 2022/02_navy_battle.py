size = int(input())
battlefield = [[x for x in input()] for x in range(size)]

row, col = 0, 0
for i in range(size):
    if "S" in battlefield[i]:
        row = i
        col = battlefield[i].index("S")
        break

position = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}


def check(current_row, current_col, mine, cruiser):
    battlefield[current_row][current_col] = "-"
    current_row += position[command]["row"]
    current_col += position[command]["col"]
    pos = battlefield[current_row][current_col]
    if pos == "*":
        mine += 1
    elif pos == "C":
        cruiser += 1
    battlefield[current_row][current_col] = "S"
    return current_row, current_col, mine, cruiser


hit_by_mine, destroyed_cruiser = 0, 0
while True:
    command = input()
    row, col, hit_by_mine, destroyed_cruiser = check(row, col, hit_by_mine, destroyed_cruiser)
    if hit_by_mine == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break

    if destroyed_cruiser == 3:
        print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

[print(*x, sep="") for x in battlefield]
