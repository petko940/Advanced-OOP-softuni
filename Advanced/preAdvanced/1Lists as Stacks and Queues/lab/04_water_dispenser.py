quantity_of_water = int(input())

people = []
while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    command = input()
    if command == "End":
        print(f"{quantity_of_water} liters left")
        break

    if "refill" in command:
        text, litters = [int(x) if x.isdigit() else x for x in command.split()]
        quantity_of_water += litters
    else:
        command = int(command)
        if quantity_of_water >= command:
            print(f"{people[0]} got water")
            people.pop(0)
            quantity_of_water -= command
        else:
            print(f"{people[0]} must wait")
            people.pop(0)
