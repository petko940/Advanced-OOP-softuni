first_name, second_name = [x for x in input().split(", ")]
size = 6
maze = [[x for x in input().split()] for x in range(size)]

rest1, rest2 = 0, 0
first, second = True, False
while True:
    coordinates = input()
    if first:
        first_row, first_col = int(coordinates[1]), int(coordinates[4])
        if rest1 == 1:
            rest1 = 0
            first, second = False, True
            continue
        elif maze[first_row][first_col] == "E":
            print(f"{first_name} found the Exit and wins the game!")
            break
        elif maze[first_row][first_col] == "T":
            print(f"{first_name} is out of the game! The winner is {second_name}.")
            break
        elif maze[first_row][first_col] == "W":
            print(f"{first_name} hits a wall and needs to rest.")
            rest1 += 1
            first, second = False, True
            continue
        else:
            first, second = False, True
            continue
    if second:
        second_row, second_col = int(coordinates[1]), int(coordinates[4])
        if rest2 == 1:
            rest2 = 0
            first, second = True, False
        elif maze[second_row][second_col] == "E":
            print(f"{second_name} found the Exit and wins the game!")
            break
        elif maze[second_row][second_col] == "T":
            print(f"{second_name} is out of the game! The winner is {first_name}.")
            break
        elif maze[second_row][second_col] == "W":
            print(f"{second_name} hits a wall and needs to rest.")
            rest2 += 1
            first, second = True, False
        else:
            first, second = True, False
