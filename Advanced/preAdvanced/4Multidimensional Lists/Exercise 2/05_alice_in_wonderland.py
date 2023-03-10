def move_up(a_row, a_col, bags, check):
    if 0 <= a_row - 1:
        a_row -= 1
        if matrix[a_row][a_col] == "R":
            check = True
        elif matrix[a_row][a_col] == ".":
            pass
        elif matrix[a_row][a_col] == "*":
            pass
        else:
            bags += int(matrix[a_row][a_col])
        matrix[a_row][a_col] = "*"
    else:
        check = True
    return a_row, a_col, bags, check


def move_down(a_row, a_col, bags, check):
    if a_row + 1 < size:
        a_row += 1
        if matrix[a_row][a_col] == "R":
            check = True
        elif matrix[a_row][a_col] == ".":
            pass
        elif matrix[a_row][a_col] == "*":
            pass
        else:
            bags += int(matrix[a_row][a_col])
        matrix[a_row][a_col] = "*"
    else:
        check = True
    return a_row, a_col, bags, check


def move_left(a_row, a_col, bags, check):
    if 0 <= a_col - 1:
        a_col -= 1
        if matrix[a_row][a_col] == "R":
            check = True
        elif matrix[a_row][a_col] == ".":
            pass
        elif matrix[a_row][a_col] == "*":
            pass
        else:
            bags += int(matrix[a_row][a_col])
        matrix[a_row][a_col] = "*"
    else:
        check = True
    return a_row, a_col, bags, check


def move_right(a_row, a_col, bags, check):
    if a_col + 1 < size:
        a_col += 1
        if matrix[a_row][a_col] == "R":
            check = True
        elif matrix[a_row][a_col] == ".":
            pass
        elif matrix[a_row][a_col] == "*":
            pass
        else:
            bags += int(matrix[a_row][a_col])
        matrix[a_row][a_col] = "*"
    else:
        check = True
    return a_row, a_col, bags, check


size = int(input())
matrix = [[x for x in input().split()] for x in range(size)]

alice_row = 0
alice_col = 0
for i in range(size):
    if "A" in matrix[i]:
        alice_row = i
        alice_col = matrix[i].index("A")

is_rabbit = False
sum_bags = 0
matrix[alice_row][alice_col] = "*"
while True:
    command = input()
    if command == "up":
        alice_row, alice_col, sum_bags, is_rabbit = move_up(alice_row, alice_col, sum_bags, is_rabbit)
    elif command == "down":
        alice_row, alice_col, sum_bags, is_rabbit = move_down(alice_row, alice_col, sum_bags, is_rabbit)
    elif command == "left":
        alice_row, alice_col, sum_bags, is_rabbit = move_left(alice_row, alice_col, sum_bags, is_rabbit)
    elif command == "right":
        alice_row, alice_col, sum_bags, is_rabbit = move_right(alice_row, alice_col, sum_bags, is_rabbit)

    if sum_bags >= 10:
        print("She did it! She went to the party.")
        break

    if is_rabbit:
        print("Alice didn't make it to the tea party.")
        break

for i in matrix:
    print(*i)
