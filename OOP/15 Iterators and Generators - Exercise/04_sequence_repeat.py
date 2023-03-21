class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start = -1
        self.check_end = 0

    def __iter__(self):
        return self

    def __next__(self):
        len_sequence = len(self.sequence)
        self.check_end += 1
        while self.check_end <= self.number:
            self.start += 1

            if self.start == len_sequence:
                self.start = 0
            return self.sequence[self.start]
        raise StopIteration
