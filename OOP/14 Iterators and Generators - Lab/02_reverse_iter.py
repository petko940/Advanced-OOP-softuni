class reverse_iter:
    def __init__(self, args):
        self.args: list = args
        self.i = len(args) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            output = self.args[self.i]
            self.i -= 1
            return output
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
