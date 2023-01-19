class Parking:
    def __init__(self):
        self.data = set()

    def cars(self):
        n = int(input())
        for _ in range(n):
            move, number = [x for x in input().split(", ")]
            if move == "IN":
                self.data.add(number)
            else:
                self.data.remove(number)

    def __str__(self):
        if self.data:
            return '\n'.join([str(x) for x in self.data])
        else:
            return f"Parking Lot is Empty"


new_cars = Parking()
new_cars.cars()
print(new_cars)
