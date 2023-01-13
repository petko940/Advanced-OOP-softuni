from collections import deque

cups_capacity = deque([int(x) for x in input().split()])  # in litters
filled_bottles = deque([int(x) for x in input().split()])  # in litters

wasted_water = 0
while filled_bottles and cups_capacity:
    cup = cups_capacity.popleft()
    bottle = filled_bottles.pop()

    if cup <= bottle:
        wasted_water += bottle - cup
    else:
        cups_capacity.appendleft(cup - bottle)

if cups_capacity:
    print(f"Cups: {' '.join([str(x) for x in cups_capacity])}")
else:
    print(f"Bottles: {' '.join([str(x) for x in filled_bottles])}")

print(f"Wasted litters of water: {wasted_water}")
