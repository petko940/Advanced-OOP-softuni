from collections import deque

quantity = int(input())
sequence = deque(int(x) for x in input().split())

print(max(sequence))

while sequence:
    order = sequence.popleft()
    if quantity - order >= 0:
        quantity -= order
    else:
        print("Orders left:", order, *sequence)
        break
else:
    print("Orders complete")
