from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
value_of_the_intelligence = int(input())

current_barrel = size_barrel
while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()
    current_barrel -= 1
    if current_barrel < 0:
        current_barrel = size_barrel
        bullets.append(bullet)
        locks.appendleft(lock)
        print("Reloading!")
    elif bullet > lock:
        print("Ping!")
        locks.appendleft(lock)
    else:
        print("Bang!")




