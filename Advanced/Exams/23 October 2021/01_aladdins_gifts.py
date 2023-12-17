from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

gemstone, porcelain_sculpture, gold, diamond_jewellery = 0, 0, 0, 0
while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()

    result = material + magic_level
    if result < 100:
        if result % 2 == 0:
            result = material * 2 + magic_level * 3
        else:
            result = 2 * (material + magic_level)

    elif result >= 500:
        result /= 2

    if 100 <= result < 200:
        gemstone += 1

    elif 200 <= result < 300:
        porcelain_sculpture += 1

    elif 300 <= result < 400:
        gold += 1

    elif 400 <= result < 500:
        diamond_jewellery += 1

if (gemstone and porcelain_sculpture) or (gold and diamond_jewellery):
    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

output = {
    "Gemstone": gemstone,
    "Porcelain Sculpture": porcelain_sculpture,
    "Gold": gold,
    "Diamond Jewellery": diamond_jewellery,
}

for k, v in sorted(output.items(), key=lambda x: x[0]):
    if v:
        print(f"{k}: {v}")
