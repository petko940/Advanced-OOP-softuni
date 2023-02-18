from collections import deque

textiles = deque([int(x) for x in input().split()])
# medicaments = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

healing_items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100
}
output = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}
while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    result = textile + medicament

    for key, value in healing_items.items():
        if result == value:
            output[key] += 1
            break
    else:
        if result > 100:
            output["MedKit"] += 1
            result -= 100
            medicaments[-1] += result
        else:
            medicaments.append(medicament + 10)

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for k, v in sorted(output.items(), key=lambda x: (-x[1], x[0])):
    if v:
        print(f"{k} - {v}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments[::-1]])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
