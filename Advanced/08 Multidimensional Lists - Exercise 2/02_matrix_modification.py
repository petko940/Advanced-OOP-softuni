size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    commands = input()
    if commands == "END":
        break
    command, *info = [int(x) if x[-1].isdigit() else x for x in commands.split()]
    if 0 <= info[0] < size and 0 <= info[1] < size:
        if command.startswith('Add'):
            matrix[info[0]][info[1]] += info[2]
        else:
            matrix[info[0]][info[1]] -= info[2]
    else:
        print('Invalid coordinates')

[print(*x) for x in matrix]
