from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = deque([int(x) for x in input().split(', ')])

total_time = 0
while taxis and customers:
    customer = customers.popleft()  # time it takes to drive the customer t
    taxi = taxis.pop()  # how much time they can drive, before fill

    result = customer + taxi
    if taxi >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print(f"""All customers were driven to their destinations
Total time: {total_time} minutes""")

else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers])}')
