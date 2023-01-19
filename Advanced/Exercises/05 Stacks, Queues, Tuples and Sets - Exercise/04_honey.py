from collections import deque

symbols_data = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b > 0 else 0,
}
working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

total_honey = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar >= first_bee:
        total_honey += abs(symbols_data[symbols.popleft()](first_bee, last_nectar))
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
