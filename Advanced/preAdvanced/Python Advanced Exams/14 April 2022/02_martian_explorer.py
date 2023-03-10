"""
    • One rover - marked with the letter "E"
    • Water deposit (one or many) - marked with the letter "W"
    • Metal deposit (one or many) - marked with the letter "M"
    • Concrete deposit (one or many) - marked with the letter "C"
    • Rock (one or many) - marked with the letter "R"
    • Empty positions will be marked with "-"
"""

position = {
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
}

size = 6
matrix = [[x for x in input().split()] for x in range(size)]
positions_row, positions_col = 0, 0
for i in range(size):
    if "E" in matrix[i]:
        positions_row = i
        positions_col = matrix[i].index("E")
        break


def movement(position_row, position_col):
    position_row += position[command]["row"]
    position_col += position[command]["col"]
    if position_row < 0:
        position_row = 5
    elif position_row > 5:
        position_row = 0
    if position_col < 0:
        position_col = 5
    elif position_col > 5:
        position_col = 0

    pos = matrix[position_row][position_col]
    if pos == "W":
        counts["water"] += 1
        print(f"Water deposit found at ({position_row}, {position_col})")
    elif pos == "M":
        counts["metal"] += 1
        print(f"Metal deposit found at ({position_row}, {position_col})")
    elif pos == "C":
        counts["concrete"] += 1
        print(f"Concrete deposit found at ({position_row}, {position_col})")
    elif pos == "R":
        print(f"Rover got broken at ({position_row}, {position_col})")
        return position_row, position_col
    matrix[position_row][position_col] = "-"
    return position_row, position_col


counts = {"water": 0, "metal": 0, "concrete": 0}
commands = input().split(", ")
for command in commands:
    positions_row, positions_col = movement(positions_row, positions_col)
    if matrix[positions_row][positions_col] == "R":
        if counts["water"] and counts["metal"] and counts["concrete"]:
            print("Area suitable to start the colony.")
        else:
            print("Area not suitable to start the colony.")
        break
else:
    if counts["water"] and counts["metal"] and counts["concrete"]:
        print("Area suitable to start the colony.")
    else:
        print("Area not suitable to start the colony.")

