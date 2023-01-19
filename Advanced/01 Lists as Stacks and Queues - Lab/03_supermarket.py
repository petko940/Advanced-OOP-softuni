from collections import deque

customers = deque()
COMMAND_END, COMMAND_PAID = "End", "Paid"
while True:
    name = input()
    if name == COMMAND_END:
        print(f"{len(customers)} people remaining.")
        break
    elif name == COMMAND_PAID:
        for _ in range(len(customers)):
            print(customers.popleft())
    else:
        customers.append(name)
