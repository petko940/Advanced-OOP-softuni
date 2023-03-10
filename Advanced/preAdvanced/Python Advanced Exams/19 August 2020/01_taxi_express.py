from collections import deque

# колко време е необходимо, за да закара клиента до неговата/нейната дестинация.
customers = deque([int(x) for x in input().split(", ")])
# таксита показва колко време могат да карат,
taxis = deque([int(x) for x in input().split(", ")])

total_time = 0
while customers and taxis:
    first_customer = customers.popleft()
    last_taxi = taxis.pop()
    if last_taxi >= first_customer:
        total_time += first_customer
    else:
        customers.appendleft(first_customer)

if not customers:
    print(f"""All customers were driven to their destinations
Total time: {total_time} minutes""")
else:
    print(f"""Not all customers were driven to their destinations
Customers left: {', '.join([str(x) for x in customers])}""")
