directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
racing_number = input()

matrix = []
tunnel_pos = []
car_pos = [0, 0]
for i in range(size):
    matrix.append(input().split())
    if 'T' in matrix[i]:
        tunnel_pos.append((i, matrix[i].index("T")))

kilometers = 0
while True:
    direction = input()
    if direction.startswith("End"):
        break

    car_pos[0] += directions[direction][0]
    car_pos[1] += directions[direction][1]
    if matrix[car_pos[0]][car_pos[1]] == ".":
        kilometers += 10
    elif matrix[car_pos[0]][car_pos[1]] == "T":
        kilometers += 30
        matrix[car_pos[0]][car_pos[1]] = "."
        car_pos[0] = tunnel_pos[1][0]
        car_pos[1] = tunnel_pos[1][1]
        matrix[car_pos[0]][car_pos[1]] = "."
    elif matrix[car_pos[0]][car_pos[1]] == "F":
        kilometers += 10
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

if direction.startswith("End"):
    print(f"Racing car {racing_number} DNF.")
    matrix[car_pos[0]][car_pos[1]] = "C"

print(f"Distance covered {kilometers} km.")
[print(*x, sep="") for x in matrix]
