rows, columns = [int(x) for x in input().split()]

start_char = ord('a')
i = 0

for row in range(rows):
    for col in range(columns):
        print(f"{chr(start_char)}{chr(start_char + col)}{chr(start_char)}", end=" ")
    start_char += 1
    print()
