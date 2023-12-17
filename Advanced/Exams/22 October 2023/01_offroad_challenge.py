from collections import deque

fuel = deque(int(x) for x in input().split())
consumption_index = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())
n = 1

altitudes = len(fuel)
while fuel:
    current_fuel = fuel.pop()
    current_consumption = consumption_index.popleft()
    result = current_fuel - current_consumption

    current_fuel_needed = fuel_needed.popleft()

    if result < current_fuel_needed:
        print(f"John did not reach: Altitude {n}")
        break

    print(f"John has reached: Altitude {n}")
    n += 1

if fuel and n == 1:
    print(f"John failed to reach the top.\n"
          f"John didn't reach any altitude.")
elif n > 1:
    print(f"John failed to reach the top.\n"
          f"Reached altitudes: {', '.join(f'Altitude {x}' for x in range(1, n))}")
else:
    print(f"John has reached all the altitudes and managed to reach the top!")
