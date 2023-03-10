from collections import deque

milligrams_coffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])

maximum_caffeine = 300
caffeine_taken = 0

while milligrams_coffeine and energy_drinks:
    last_milligram = milligrams_coffeine.pop()
    first_energy_drink = energy_drinks.popleft()

    multiply = last_milligram * first_energy_drink
    if multiply + caffeine_taken <= 300:
        caffeine_taken += multiply
    else:
        energy_drinks.append(first_energy_drink)
        caffeine_taken -= 30
        if caffeine_taken < 0:
            caffeine_taken = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_taken} mg caffeine.")
