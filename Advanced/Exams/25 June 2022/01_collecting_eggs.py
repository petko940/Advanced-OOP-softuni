from collections import deque

eggs_size = deque([int(x) for x in input().split(', ')])
pieces_of_paper_size = deque([int(x) for x in input().split(', ')])

boxes = 0
while eggs_size and pieces_of_paper_size:
    egg = eggs_size.popleft()
    piece = pieces_of_paper_size.pop()
    if egg == 13:
        pieces_of_paper_size.append(piece)
        pieces_of_paper_size[0], pieces_of_paper_size[-1] = \
            pieces_of_paper_size[-1], pieces_of_paper_size[0]
    elif egg <= 0:
        pieces_of_paper_size.append(piece)
    elif egg + piece <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f'Eggs left: {", ".join([str(x) for x in eggs_size])}')

if pieces_of_paper_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in pieces_of_paper_size])}")
