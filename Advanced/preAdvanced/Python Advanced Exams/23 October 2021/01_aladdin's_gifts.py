from collections import deque


def check(gem, sculpt, gold, jewel, sum):
    if 100 < sum < 500:
        if 100 <= sum <= 199:
            gem += 1
        elif 200 <= sum <= 299:
            sculpt += 1
        elif 300 <= sum <= 399:
            gold += 1
        elif 400 <= sum <= 499:
            jewel += 1
    return gem, sculpt, gold, jewel


materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

gemstone, sculpture = 0, 0
gold, jewellery = 0, 0

while len(materials) and len(magic_levels):
    last_material = materials.pop()
    first_magic_level = magic_levels.popleft()
    sum = last_material + first_magic_level
    if sum < 100:
        if sum % 2 == 0:
            sum = 2 * last_material + 3 * first_magic_level
            gemstone, sculpture, gold, jewellery = check(gemstone, sculpture, gold, jewellery, sum)
        else:
            sum *= 2
            gemstone, sculpture, gold, jewellery = check(gemstone, sculpture, gold, jewellery, sum)
    elif sum > 499:
        sum /= 2
        gemstone, sculpture, gold, jewellery = check(gemstone, sculpture, gold, jewellery, sum)
    else:
        gemstone, sculpture, gold, jewellery = check(gemstone, sculpture, gold, jewellery, sum)

if (gemstone and sculpture) or (gold and jewellery):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

if jewellery:
    print(f"Diamond Jewellery: {jewellery}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if sculpture:
    print(f"Porcelain Sculpture: {sculpture}")
