from collections import deque

milligrams_caffeine = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])

maximum_caffeine = 300
total_caffeine = 0

while milligrams_caffeine and energy_drinks:
    last_milligrams_caffeine = milligrams_caffeine.pop()
    first_energy_drink = energy_drinks.popleft()
    sum = last_milligrams_caffeine * first_energy_drink
    if total_caffeine + sum <= 300:
        total_caffeine += sum
    else:
        energy_drinks.append(first_energy_drink)
        total_caffeine -= 30 if total_caffeine > 0 else 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
