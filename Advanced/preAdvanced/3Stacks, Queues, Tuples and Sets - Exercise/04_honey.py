from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

result = []
while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        res = 0
        sym = symbols.popleft()
        if sym == "+":
            res = current_bee + current_nectar
        elif sym == "-":
            res = current_bee - current_nectar
        elif sym == "*":
            res = current_bee * current_nectar
        elif sym == "/":
            if current_nectar != 0:
                res = current_bee / current_nectar
        result.append(abs(res))
    else:
        working_bees.appendleft(current_bee)

total_honey = sum(result)
print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
