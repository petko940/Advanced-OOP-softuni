from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups_milk = deque([int(x) for x in input().split(", ")])

count = 0
while len(chocolates) > 0 and len(cups_milk) > 0:
    chocolate = chocolates.pop()
    cup = cups_milk.popleft()
    if chocolate == cup:
        count += 1
    else:
        if cup > 0:
            cups_milk.appendleft(cup)
        if chocolate > 0:
            chocolate -= 5
            chocolates.append(chocolate)
    if count == 5:
        break

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(map(str, cups_milk))}")
else:
    print(f"Milk: empty")
