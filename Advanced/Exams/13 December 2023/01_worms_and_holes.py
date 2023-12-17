from collections import deque

worm_size = deque(int(x) for x in input().split())  # last
hole_size = deque(int(x) for x in input().split())  # first
match = 0
worms_count = len(worm_size)

while worm_size and hole_size:
    worm = worm_size.pop()
    hole = hole_size.popleft()

    if worm != hole:
        worm -= 3
        if worm <= 0:
            continue
        worm_size.append(worm)
    else:
        match += 1

if match:
    print(f"Matches: {match}")
else:
    print("There are no matches.")

if not worm_size:
    if match == worms_count:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in worm_size)}")

if not hole_size:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in hole_size)}")
