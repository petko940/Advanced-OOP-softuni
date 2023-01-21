from collections import deque

rows, columns = [int(x) for x in input().split()]

word = input()
word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < columns:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for x in range(columns)], sep="")
    else:
        print(*[word_copy.popleft() for x in range(columns)][::-1], sep="")
