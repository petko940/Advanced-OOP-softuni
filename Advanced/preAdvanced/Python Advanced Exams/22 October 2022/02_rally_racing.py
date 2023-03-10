size = int(input())
racing_car_number = input()
matrix = [[x for x in input().split()] for x in range(size)]

final_row, final_col = 0, 0

tunnel = []
for i in range(size):
    if "F" in matrix[i]:
        final_row, final_col = i, matrix[i].index("F")
    if "T" in matrix[i]:
        for index, value in enumerate(matrix[i]):
            if value == "T":
                tunnel.append(i)
                tunnel.append(index)

tunnel1_row, tunnel1_col = tunnel[0], tunnel[1]
tunnel2_row, tunnel2_col = tunnel[2], tunnel[3]

km = 0
car_row, car_col = 0, 0

positions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]}


def check(row, col, km_passed, end):
    if matrix[row][col] == ".":
        km_passed += 10

    elif row == tunnel1_row and col == tunnel1_col:
        matrix[row][col] = "."
        km_passed += 30
        row, col = tunnel2_row, tunnel2_col
        matrix[row][col] = "."

    elif matrix[row][col] == "F":
        matrix[row][col] = "C"
        print(f"Racing car {racing_car_number} finished the stage!")
        end = True
        km_passed += 10
    return row, col, km_passed, end


end = False
while True:
    command = input()
    if command == "End":
        matrix[car_row][car_col] = "C"
        print(f"Racing car {racing_car_number} DNF.")
        break

    if command == "up":
        car_row += positions[command][0]
    elif command == "down":
        car_row += positions[command][0]
    elif command == "left":
        car_col += positions[command][1]
    elif command == "right":
        car_col += positions[command][1]
    car_row, car_col, km, end = check(car_row, car_col, km, end)

    if end:
        break

print(f"Distance covered {km} km.")
for x in matrix:
    print(*x, sep="")
