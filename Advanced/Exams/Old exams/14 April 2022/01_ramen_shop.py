from collections import deque

bowls = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while bowls and customers:
    bowl = bowls.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowls.append(bowl - customer)
    elif bowl < customer:
        customers.appendleft(customer - bowl)

if bowls:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls])}")
elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("Great job! You served all the customers.")
