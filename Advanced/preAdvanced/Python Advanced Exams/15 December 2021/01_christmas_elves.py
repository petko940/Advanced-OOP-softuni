from collections import deque

energy = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

toys = 0
counter = 0
energy_spent = 0
while materials and energy:
    while energy[0] < 5:
        energy.popleft()
        if len(energy) == 0:
            break
    if len(energy) == 0:
        break
    counter += 1
    if counter % 3 != 0:
        if energy[0] >= materials[-1]:
            if counter % 5 == 0:
                energy[0] -= materials[-1]
            else:
                energy[0] -= materials[-1] - 1
                toys += 1
            energy_spent += materials[-1]
            materials.pop()
            energy.append(energy.popleft())
        else:
            energy[0] *= 2
            energy.append(energy.popleft())
    elif counter % 3 == 0:
        if energy[0] >= materials[-1] * 2:
            if counter % 5 == 0:
                energy[0] -= materials[-1] * 2
            else:
                energy[0] -= materials[-1] * 2 - 1
                toys += 2
            energy_spent += materials[-1] * 2
            materials.pop()
            energy.append(energy.popleft())
        else:
            energy[0] *= 2
            energy.append(energy.popleft())

print(f"Toys: {toys}")
print(f"Energy: {energy_spent}")
if energy:
    print(f"Elves left: {', '.join([str(x) for x in energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")