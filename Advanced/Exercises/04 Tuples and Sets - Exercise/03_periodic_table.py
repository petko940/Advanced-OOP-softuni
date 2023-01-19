class PeriodicTable:
    def __init__(self, number):
        self.number = number
        self.data = set()

    def fill_data(self):
        for _ in range(self.number):
            items = input().split()
            for item in items:
                self.data.add(item)

    def __repr__(self):
        return '\n'.join(self.data)


chemical_elements = PeriodicTable(int(input()))
chemical_elements.fill_data()
print(chemical_elements)
