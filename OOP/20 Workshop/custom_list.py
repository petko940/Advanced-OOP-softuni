import sys


class CustomList:
    def __init__(self):
        self.list = []

    def append(self, value):
        self.list.append(value)
        return self.list

    def remove(self, index):
        removed = self.list[index]
        self.list.pop(index)
        return removed

    def get(self, index):
        return self.list[index]

    def extend(self, iterable):
        new_list = self.list.extend(iterable)
        return new_list

    def insert(self, index, value):
        self.list.insert(index, value)
        return self.list

    def pop(self):
        return self.list.pop()

    def clear(self):
        self.list.clear()

    def index(self, value):
        return self.list.index(value)

    def count(self, value):
        return self.list.count(value)

    def reverse(self):
        self.list.reverse()
        return self.list

    def copy(self):
        copy_list = self.list.copy()
        return copy_list

    def size(self):
        return len(self.list)

    def add_first(self, value):
        self.list.insert(0, value)

    def dictionize(self):
        dictionized_list = {}
        if len(self.list) % 2 != 0:
            self.list.append(' ')
            for x in range(0, len(self.list) - 1, 2):
                dictionized_list[self.list[x]] = self.list[x + 1]
            self.list.remove(' ')

        else:
            for x in range(0, len(self.list) - 1, 2):
                dictionized_list[self.list[x]] = self.list[x + 1]

        return dictionized_list

    def move(self, amount):
        numbers = []
        for x in self.list[:amount]:
            numbers.append(x)
            self.list.remove(x)
        self.list.extend(numbers)
        return self.list

    def sum(self):
        sum = 0
        for x in self.list:
            if isinstance(x, str):
                sum += len(x)
            else:
                sum += x

        return sum

    def overbound(self):
        biggest_value = -sys.maxsize
        for x in self.list:
            if isinstance(x, str):
                if len(x) > biggest_value:
                    biggest_value = self.list.index(x)
            else:
                if x > biggest_value:
                    biggest_value = self.list.index(x)
        return biggest_value

    def underbound(self):
        smallest_value = sys.maxsize
        for x in self.list:
            if isinstance(x, str):
                if len(x) < smallest_value:
                    smallest_value = self.list.index(x)
            else:
                if x < smallest_value:
                    smallest_value = self.list.index(x)
        return smallest_value
