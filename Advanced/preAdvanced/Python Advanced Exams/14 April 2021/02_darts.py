player1, player2 = [x for x in input().split(", ")]
matrix = [[x for x in input().split()] for x in range(7)]

player1_throws, player2_throws = 0, 0
player1_points, player2_points = 501, 501
who_play = 0  # player1 = even / player2 = odd
while True:
    coordinates = input().replace("(", '').replace(")", '').split(", ")
    row, col = int(coordinates[0]), int(coordinates[1])
    # outside ----
    if row >= 7 or col >= 7:
        if who_play % 2 == 0:
            player1_throws += 1
        else:
            player2_throws += 1
        who_play += 1
        continue

    if who_play % 2 == 0:
        player1_throws += 1
    elif who_play % 2 != 0:
        player2_throws += 1

    current_sum = [int(matrix[row][0]), int(matrix[row][-1]),
                   int(matrix[0][col]), int(matrix[-1][col])]
    shot = 0
    # if coordinates is digit
    if matrix[row][col].isdigit():
        if who_play % 2 == 0:
            player1_points -= int(matrix[row][col])
        elif who_play % 2 != 0:
            player2_points -= int(matrix[row][col])
    else:  # if coordinates is not digit
        if matrix[row][col] == "D":
            shot = sum(current_sum) * 2
        elif matrix[row][col] == "T":
            shot = sum(current_sum) * 3
        elif matrix[row][col] == "B":
            if who_play % 2 == 0:
                print(f"{player1} won the game with {player1_throws} throws!")
            elif who_play % 2 != 0:
                print(f"{player2} won the game with {player2_throws} throws!")
            break
        if who_play % 2 == 0:
            player1_points -= shot
        elif who_play % 2 != 0:
            player2_points -= shot

    if player1_points <= 0:
        print(f"{player1} won the game with {player1_throws} throws!")
        break
    elif player2_points <= 0:
        print(f"{player2} won the game with {player2_throws} throws!")
        break

    who_play += 1
