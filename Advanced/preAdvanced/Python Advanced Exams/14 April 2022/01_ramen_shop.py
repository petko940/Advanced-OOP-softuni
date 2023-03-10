from collections import deque

bowls_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while len(bowls_ramen) > 0 and len(customers) > 0:
    ramen = bowls_ramen.pop()
    customer = customers.popleft()
    if ramen > customer:
        bowls_ramen.append(ramen - customer)
    elif ramen < customer:
        customers.appendleft(customer - ramen)

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(x) for x in customers])}")
