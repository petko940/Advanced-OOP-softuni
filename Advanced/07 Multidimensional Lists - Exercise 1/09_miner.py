movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
commands = [x for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(size)]

start_row, start_col = 0, 0
all_coal, collected_coal = 0, 0

for m in range(size):
    if 's' in matrix[m]:
        start_row = m
        start_col = matrix[m].index('s')
        matrix[start_row][start_col] = "*"

    all_coal += matrix[m].count('c')


def collected_all():
    return f"You collected all coal! ({start_row}, {start_col})"


def end():
    return f"Game over! ({start_row}, {start_col})"


def check_bounds(row, col):

    if 0 <= row < size and 0 <= col < size:
        return True
    return False


for command in commands:
    if check_bounds(start_row + movement[command][0], start_col + movement[command][1]):
        start_row += movement[command][0]
        start_col += movement[command][1]

        if matrix[start_row][start_col] == "c":
            matrix[start_row][start_col] = '*'
            collected_coal += 1
            if collected_coal == all_coal:
                print(collected_all())
                break

        elif matrix[start_row][start_col] == 'e':
            print(end())
            break
else:
    print(f"{all_coal - collected_coal} pieces of coal left. ({start_row}, {start_col})")
