from collections import deque

quantity_food = int(input())
order = deque([int(x) for x in input().split()])

print(max(order))

while order:
    current_order = order.popleft()
    if quantity_food >= current_order:
        quantity_food -= current_order
    else:
        order.appendleft(current_order)
        print(f"Orders left: {' '.join([str(x) for x in order])}")
        break
else:
    print("Orders complete")
