from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees = deque([int(x) for x in input().split(', ')])

total_count = 0
while orders and employees:
    order = orders.popleft()
    if order > 10 or 0 >= order:
        continue

    employee = employees.pop()

    if order > employee:
        order -= employee
        total_count += employee
        orders.appendleft(order)
    else:
        total_count += order

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_count}')
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
