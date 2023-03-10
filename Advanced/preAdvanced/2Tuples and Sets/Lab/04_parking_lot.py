def enter(number):
    cars.add(number)


def exit(number):
    cars.remove(number)


cars = set()
number_commands = int(input())

for _ in range(number_commands):
    command , car_number = input().split(", ")
    if command == "IN":
        enter(car_number)
    else:
        exit(car_number)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
