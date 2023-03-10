from collections import deque

lists = input().split("|")
new_lists = []
for lst in lists:
    new_lists.append(lst.strip().split())

output = deque()
for x in new_lists[::-1]:
    for y in x:
        output.append(int(y))

print(*output)
