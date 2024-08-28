from collections import deque

bee_groups = deque([int(x) for x in input().split()])
eaters = deque([int(x) for x in input().split()])

while bee_groups and eaters:
    bee = bee_groups.popleft()
    eater = eaters.pop()

    while bee > 0 and eater > 0:
        if eater * 7 <= bee:
            bee -= eater * 7
            eater = 0
        else:
            eater -= (bee // 7)
            bee = 0

    if bee > 0 and eater == 0:
        bee_groups.append(bee)
    elif bee == 0 and eater > 0:
        eaters.append(eater)

print("The final battle is over!")
if bee_groups:
    print(f"Bee groups left: {', '.join(str(x) for x in bee_groups)}")
elif eaters:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in eaters)}")
else:
    print(f"But no one made it out alive!")
