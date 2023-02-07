from collections import deque

fireworks = deque([int(x) for x in input().split(", ")])
explosives = deque([int(x) for x in input().split(", ")])

palm, willow, crossette = 0, 0, 0

while fireworks and explosives:
    if fireworks[0] <= 0:
        fireworks.popleft()
        continue
    elif explosives[-1] <= 0:
        explosives.pop()
        continue

    firework = fireworks.popleft()
    explosive = explosives.pop()

    result = firework + explosive

    if result % 3 == 0 and result % 5 != 0:
        palm += 1
    elif result % 5 == 0 and result % 3 != 0:
        willow += 1
    elif result % 5 == 0 and result % 3 == 0:
        crossette += 1

    else:
        fireworks.append(firework - 1)
        explosives.append(explosive)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        print("Congrats! You made the perfect firework show!")
        break
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")

if explosives:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosives])}")

print(f"""Palm Fireworks: {palm}
Willow Fireworks: {willow}
Crossette Fireworks: {crossette}""")
