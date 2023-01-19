from collections import deque

quantity_of_water = int(input())
names = deque()
while True:
    name = input()
    if name == "Start":
        break
    names.append(name)

REFILL, END = "refill", "End"

while True:
    command = input()
    if command.startswith(REFILL):
        liters = int(command.split()[1])
        quantity_of_water += liters
    elif command == END:
        print(f"{quantity_of_water} liters left")
        break
    else:
        liters = int(command)
        if liters <= quantity_of_water:
            quantity_of_water -= liters
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait")
