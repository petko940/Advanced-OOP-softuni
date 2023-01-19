class BattleNames:
    def __init__(self, number):
        self.number = number
        self.odd_set = set()
        self.even_set = set()

    def ascii_value(self):
        for row in range(1, self.number + 1):
            name = input()
            sum_ascii = 0
            for char in name:
                sum_ascii += ord(char)
            sum_ascii //= row
            if sum_ascii % 2 == 0:
                self.even_set.add(sum_ascii)
            else:
                self.odd_set.add(sum_ascii)

    def output(self):
        if sum(self.odd_set) == sum(self.even_set):
            return ', '.join([str(x) for x in self.odd_set.union(self.even_set)])
        elif sum(self.odd_set) > sum(self.even_set):
            return ', '.join([str(x) for x in self.odd_set.difference(self.even_set)])
        else:
            return ', '.join([str(x) for x in self.odd_set.symmetric_difference(self.even_set)])


names = BattleNames(int(input()))
names.ascii_value()
print(names.output())
