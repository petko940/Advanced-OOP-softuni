dictionary = {
    "rows": [8, 7, 6, 5, 4, 3, 2, 1],
    "cols": ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h']
}

matrix = [[x for x in input().split()] for _ in range(8)]

white, black = [], []
for i in range(8):
    if 'w' in matrix[i]:
        white = [i, matrix[i].index('w')]
        matrix[i][white[1]] = '-'
    if 'b' in matrix[i]:
        black = [i, matrix[i].index('b')]

white_or_black = True  # white true , black false
while white[0] != 0 and black[0] != 7:
    if white_or_black:
        if white[0] > black[0]:
            if 'b' in matrix[white[0] - 1]:
                if 'b' == matrix[white[0] - 1][white[1] - 1] or \
                        'b' == matrix[white[0] - 1][white[1] + 1]:
                    r = dictionary['rows'][black[0]]
                    c = dictionary['cols'][black[1]]
                    print(f"Game over! White win, capture on {c}{r}.")
                    break
        matrix[white[0]][white[1]] = '-'
        white[0] -= 1
        matrix[white[0]][white[1]] = 'w'
        white_or_black = False
    else:
        if white[0] > black[0]:
            if 'w' in matrix[black[0] + 1]:
                if 'w' == matrix[black[0] + 1][black[1] - 1] or \
                        'w' == matrix[black[0] + 1][black[1] + 1]:
                    r = dictionary['rows'][white[0]]
                    c = dictionary['cols'][white[1]]
                    print(f"Game over! Black win, capture on {c}{r}.")
                    break
        matrix[black[0]][black[1]] = '-'
        black[0] += 1
        matrix[black[0]][black[1]] = 'b'
        white_or_black = True

else:
    if white[0] == 0:
        r = dictionary['rows'][white[0]]
        c = dictionary['cols'][white[1]]
        print(f"Game over! White pawn is promoted to a queen at {c}{r}.")
    else:
        r = dictionary['rows'][black[0]]
        c = dictionary['cols'][black[1]]
        print(f"Game over! Black pawn is promoted to a queen at {c}{r}.")
