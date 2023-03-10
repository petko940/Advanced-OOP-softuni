from collections import deque

petrol_pumps = int(input())
petrol = deque()

for _ in range(petrol_pumps):
    amount_petrol, distance = [int(x) for x in input().split()]
    petrol.append([amount_petrol, distance])

for attempt in range(petrol_pumps):
    tank = 0
    circle = True
    for x in petrol:
        fuel, distance = x[0], x[1]
        tank += fuel
        if distance > tank:
            circle = False
            break
        else:
            tank -= distance
    if circle:
        print(attempt)
        break
    else:
        petrol.append(petrol.popleft())


# 3
# 1 5
# 10 3
# 3 4
