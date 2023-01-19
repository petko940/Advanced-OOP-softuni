from collections import deque

number_pumps = int(input())

circle = deque()
for _ in range(number_pumps):
    amount_petrol, distance = [int(x) for x in input().split()]
    circle.append((amount_petrol, distance))

for i in range(len(circle)):
    current_circle = circle.copy()
    saved_petrol = 0
    while current_circle:
        drive = current_circle.popleft()
        if drive[0] + saved_petrol >= drive[1]:
            saved_petrol += drive[0] - drive[1]
        else:
            break
    if len(current_circle) == 0:
        print(i)
        break
    circle.rotate(-1)
