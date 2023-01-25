directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]

alice_pos = None
for i in range(size):
    if 'A' in matrix[i]:
        alice_pos = [i, matrix[i].index('A')]
        matrix[i][alice_pos[1]] = '*'

bags = 0
while bags < 10:
    movement = input()
    alice_pos[0] += directions[movement][0]
    alice_pos[1] += directions[movement][1]
    if 0 <= alice_pos[0] < size and 0 <= alice_pos[1] < size:
        if matrix[alice_pos[0]][alice_pos[1]] == 'R':
            matrix[alice_pos[0]][alice_pos[1]] = '*'
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[alice_pos[0]][alice_pos[1]].isdigit():
            bags += int(matrix[alice_pos[0]][alice_pos[1]])
        matrix[alice_pos[0]][alice_pos[1]] = '*'
    else:
        print("Alice didn't make it to the tea party.")
        break
else:
    print('She did it! She went to the party.')

[print(*x) for x in matrix]
