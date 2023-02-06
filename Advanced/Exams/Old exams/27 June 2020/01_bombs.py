from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = deque([int(x) for x in input().split(", ")])

bombs = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Bombs": [120, 0],
}

datura_bombs, cherry_bombs, smoke_bombs = 0, 0, 0
bombs_filled = False
while effects and casings and bombs_filled == False:
    effect = effects.popleft()
    casing = casings.pop()

    result = effect + casing
    for k, v in bombs.items():
        if result == v[0]:
            v[1] += 1
            break
    else:
        casings.append(casing - 5)
        effects.appendleft(effect)

    for value in bombs.values():
        if value[1] >= 3:
            bombs_filled = True
        else:
            bombs_filled = False
            break

if bombs_filled:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print("Bomb Casings: empty")

print(f"""Cherry Bombs: {bombs["Cherry Bombs"][1]}
Datura Bombs: {bombs["Datura Bombs"][1]}
Smoke Decoy Bombs: {bombs["Smoke Bombs"][1]}
""")
