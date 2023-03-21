class countdown_iterator:
    def __init__(self, count):
        self.count = count + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > self.end:
            self.count -= 1
            return self.count

        raise StopIteration

