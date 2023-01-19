from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups = deque([int(x) for x in input().split(", ")])

prepared = 0
while prepared != 5 and chocolates and cups:
    chocolate = chocolates.pop()
    cup = cups.popleft()

    if chocolate < 1 and cup < 1:
        continue
    elif chocolate <= 0:
        cups.appendleft(cup)
        continue
    elif cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup:
        prepared += 1
    else:
        cups.append(cup)
        chocolates.append(chocolate - 5)

if prepared == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join([str(x) for x in cups])}")
else:
    print("Milk: empty")
