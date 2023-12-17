matrix = [[x for x in input().split()] for _ in range(6)]

points = 0
for _ in range(3):
    throw = [x for x in input().split(', ')]
    throw_row = int(throw[0][1:])
    throw_col = int(throw[1][:-1])
    if not (0 <= throw_row < 6 and 0 <= throw_col < 6) \
            or matrix[throw_row][throw_col] != "B":
        continue
    if matrix[throw_row][throw_col] == "B":
        for x in range(6):
            if matrix[x][throw_col].isdigit():
                points += int(matrix[x][throw_col])
            elif matrix[x][throw_col] == "B":
                matrix[x][throw_col] = '0'

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points < 200:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
