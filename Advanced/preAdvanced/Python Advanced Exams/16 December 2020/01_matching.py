from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches_count = 0
while males and females:
    if males[-1] <= 0:
        del males[-1]
        continue
    if females[0] <= 0:
        del females[0]
        continue
    if males[-1] % 25 == 0:
        del males[-1]
        del males[-1]
        continue
    if females[0] % 25 == 0:
        del females[0]
        del females[0]
        continue
    m = males.pop()
    f = females.popleft()
    if f == m:
        matches_count += 1
    else:
        males.append(m - 2)

print(f"Matches: {matches_count}")

if males:
    print(f"Males left: {', '.join([str(m) for m in males[::-1]])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(f) for f in females])}")
else:
    print("Females left: none")
