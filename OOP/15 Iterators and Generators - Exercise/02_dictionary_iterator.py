class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < len(self.dictionary) - 1:
            self.start += 1
            return self.dictionary[self.start]
        else:
            raise StopIteration
