rows, columns = [int(x) for x in input().split()]
snake = input()

matrix = []

i = 0
for row in range(rows):
    for col in range(columns):
        if i == len(snake):
            i = 0
        if row % 2 == 0:
            matrix.append(snake[i])
        else:
            matrix.insert(0, snake[i])
        i += 1
    print(*matrix, sep="")
    matrix = []
