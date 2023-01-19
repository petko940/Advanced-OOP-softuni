from collections import deque

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])

crafted_presents = {}
while materials and magic_level:
    last_box = materials.pop()
    first_magic = magic_level.popleft()
    multiplication = last_box * first_magic

    for present, value in presents.items():
        if multiplication == value:
            crafted_presents[present] = crafted_presents.get(present, 0) + 1
            break
    else:
        if multiplication < 0:
            sum_materials = last_box + first_magic
            materials.append(sum_materials)
        elif multiplication > 0:
            materials.append(last_box + 15)
        else:
            if last_box:
                materials.append(last_box)
            if first_magic:
                magic_level.appendleft(first_magic)

is_merry_christmas = False
check_if_done = set(crafted_presents.keys())
if {"Doll", "Wooden train"}.issubset(check_if_done) or \
        {"Teddy bear", "Bicycle"}.issubset(check_if_done):
    is_merry_christmas = True

if is_merry_christmas:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

[print(f"{name}: {amount}") for name, amount in sorted(crafted_presents.items())]
