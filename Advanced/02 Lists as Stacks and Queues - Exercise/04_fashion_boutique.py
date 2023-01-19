from collections import deque

clothes_in_box = deque(int(x) for x in input().split())
capacity = int(input())
current_capacity = capacity
count = 1
while clothes_in_box:
    current_cloth = clothes_in_box.pop()
    if current_cloth > capacity:
        clothes_in_box.append(current_cloth)
        count += 1
        capacity = current_capacity
    else:
        capacity -= current_cloth

print(count)
