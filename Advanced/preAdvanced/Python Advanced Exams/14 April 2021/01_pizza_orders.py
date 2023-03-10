from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = deque([int(x) for x in input().split(", ")])
total_count = 0
while len(pizza_orders) != 0 and len(employees) != 0:
    first_order = pizza_orders.popleft()
    employee = employees.pop()

    if first_order > 10 or first_order <= 0:
        employees.append(employee)
        continue

    if first_order > employee:
        pizza_orders.appendleft(first_order - employee)
        total_count += employee
    else:
        total_count += first_order

if len(pizza_orders) == 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
