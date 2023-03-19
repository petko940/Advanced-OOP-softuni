class vowels:
    def __init__(self, word: str):
        self.word = word
        self.vowels_data = ["a", "e", "i", "o", "u", "y"]
        self.end = len(word)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            index = self.start
            self.start += 1

            if self.word[index].lower() in self.vowels_data:
                return self.word[index]
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
