names = [x for x in input().split(', ')]
maze = [[x for x in input().split()] for _ in range(6)]

winner = ''
first_rest, second_rest = 0, 0


def who_win():
    if first_or_second % 2 == 0:
        return 0
    else:
        return 1


first_or_second = 0  # if name is even first
while True:
    coordinates = input()
    row, col = int(coordinates[1:2]), int(coordinates[4:-1])
    if first_rest and first_or_second % 2 == 0:
        first_rest -= 1
        first_or_second += 1
        continue
    if second_rest and first_or_second % 2 != 0:
        second_rest -= 1
        first_or_second += 1
        continue

    if maze[row][col] == 'E':
        if who_win() == 0:
            winner = names[0]
        else:
            winner = names[1]
        print(f"{winner} found the Exit and wins the game!")
        break
    elif maze[row][col] == 'T':
        if who_win() == 0:
            winner = names[1]
            print(f"{names[0]} is out of the game! The winner is {winner}.")
        else:
            winner = names[0]
            print(f"{names[1]} is out of the game! The winner is {winner}.")
        break
    elif maze[row][col] == 'W':
        if first_or_second % 2 == 0:
            print(f"{names[0]} hits a wall and needs to rest.")
            first_rest += 1
        else:
            print(f"{names[1]} hits a wall and needs to rest.")
            second_rest += 1

    first_or_second += 1
