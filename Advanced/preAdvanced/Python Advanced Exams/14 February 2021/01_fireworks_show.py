from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

palm_firework = 0
willow_firework = 0
crossette_firework = 0

is_ready = False
while len(firework_effects) > 0 and len(explosive_power) > 0:
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()
    sum = first_firework + last_explosive
    if first_firework <= 0:
        explosive_power.append(last_explosive)
        continue
    if last_explosive <= 0:
        firework_effects.appendleft(first_firework)
        continue

    if sum % 3 == 0 and sum % 5 != 0:
        palm_firework += 1
    elif sum % 3 != 0 and sum % 5 == 0:
        willow_firework += 1
    elif sum % 3 == 0 and sum % 5 == 0:
        crossette_firework += 1
    else:
        firework_effects.append(first_firework - 1)
        explosive_power.append(last_explosive)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        is_ready = True
        break

if is_ready:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f"""Palm Fireworks: {palm_firework}
Willow Fireworks: {willow_firework}
Crossette Fireworks: {crossette_firework}""")
