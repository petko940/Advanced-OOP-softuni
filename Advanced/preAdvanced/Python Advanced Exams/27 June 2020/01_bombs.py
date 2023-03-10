from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = deque([int(x) for x in input().split(", ")])

datura_bombs, cherry_bombs, smoke_bombs = 0, 0, 0
is_ready = False

while effects and casings and is_ready == False:
    first_effect = effects.popleft()
    last_casing = casings.pop()
    sum_first_last = first_effect + last_casing
    if sum_first_last == 40:
        datura_bombs += 1
    elif sum_first_last == 60:
        cherry_bombs += 1
    elif sum_first_last == 120:
        smoke_bombs += 1
    else:
        effects.appendleft(first_effect)
        casings.append(last_casing - 5)
    if datura_bombs > 2 and cherry_bombs > 2 and smoke_bombs > 2:
        is_ready = True

if is_ready:
    print("Bene! You have successfully filled the bomb pouch!")
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

print(f"""Cherry Bombs: {cherry_bombs}
Datura Bombs: {datura_bombs}
Smoke Decoy Bombs: {smoke_bombs}
""")
