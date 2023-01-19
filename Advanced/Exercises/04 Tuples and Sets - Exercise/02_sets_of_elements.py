class Elements:
    def __init__(self, len_one, len_two):
        self.len_one = len_one
        self.len_two = len_two
        self.first_set = set()
        self.second_set = set()

    def unique_elements(self):
        for _ in range(self.len_one):
            self.first_set.add(int(input()))

        for _ in range(self.len_two):
            self.second_set.add(int(input()))

    def __repr__(self):
        output = self.first_set.intersection(self.second_set)
        return '\n'.join([str(x) for x in output])


n, m = [int(x) for x in input().split()]
elements = Elements(n, m)
elements.unique_elements()
print(elements)
