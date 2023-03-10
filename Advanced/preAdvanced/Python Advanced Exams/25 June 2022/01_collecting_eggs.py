from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
piece_of_paper = deque([int(x) for x in input().split(", ")])

box = 0
while len(eggs) and len(piece_of_paper):
    egg = eggs.popleft()
    last_paper = piece_of_paper.pop()
    if egg <= 0:
        piece_of_paper.append(last_paper)
        continue

    if egg == 13:
        first_paper = piece_of_paper.popleft()
        piece_of_paper.appendleft(last_paper)
        piece_of_paper.append(first_paper)
        continue

    if egg + last_paper <= 50:
        box += 1

if box:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in piece_of_paper])}")
