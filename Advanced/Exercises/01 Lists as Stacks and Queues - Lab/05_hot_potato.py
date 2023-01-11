from collections import deque

kids_names = deque([x for x in input().split()])
toos_count = int(input())

while len(kids_names) > 1:
    kids_names.rotate(-toos_count)
    print(f"Removed {kids_names.pop()}")

print(f"Last is {kids_names[0]}")
