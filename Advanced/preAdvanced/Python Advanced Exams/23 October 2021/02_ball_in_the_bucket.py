matrix = [[x for x in input().split()] for x in range(6)]

points = 0
for _ in range(3):
    throw = input().split(", ")
    row = int(throw[0][1:])
    col = int(throw[1][:-1])
    if row < 6 and col < 6:
        if matrix[row][col] == "B":
            matrix[row][col] = "0"
            for i in range(6):
                points += int(matrix[i][col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    reward = None
    if points < 200:
        reward = "Football"
    elif points < 300:
        reward = "Teddy Bear"
    else:
        reward = "Lego Construction Set"
    print(f"Good job! You scored {points} points, and you've won {reward}.")
