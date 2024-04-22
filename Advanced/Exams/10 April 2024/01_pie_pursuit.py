from collections import deque

contestants = deque([int(x) for x in input().split()])
pieces = deque([int(x) for x in input().split()])

while contestants and pieces:
    first_contestant = contestants.popleft()
    last_pie = pieces.pop()

    if first_contestant >= last_pie:
        first_contestant -= last_pie
        if first_contestant > 0:
            contestants.append(first_contestant)
    else:
        last_pie -= first_contestant

        if pieces and last_pie == 1:
            pieces[-1] += last_pie
        else:
            pieces.append(last_pie)

if not pieces and contestants:
    print(f"We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(x) for x in contestants])}")
elif not pieces and not contestants:
    print(f"We have a champion!")
else:
    print(f"Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(x) for x in pieces])}")
