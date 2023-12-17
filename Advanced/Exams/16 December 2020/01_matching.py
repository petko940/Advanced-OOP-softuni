from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches_count = 0
while males and females:
    male = males.pop()
    if male <= 0:
        continue
    if male % 25 == 0:
        males.pop()
        continue

    female = females.popleft()
    if female <= 0:
        males.append(male)
        continue
    if female % 25 == 0:
        males.append(male)
        females.popleft()
        continue

    if male != female:
        males.append(male - 2)
    else:
        matches_count += 1

print(f"Matches: {matches_count}")

males.reverse()

if males:
    print(f"Males left: {', '.join(str(x) for x in list(males))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in list(females))}")
else:
    print("Females left: none")
