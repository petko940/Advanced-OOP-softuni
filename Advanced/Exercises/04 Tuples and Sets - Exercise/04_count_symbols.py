class CountSymbols:
    def __init__(self, text):
        self.text = text
        self.data = {}

    def occurrences(self):
        for char in self.text:
            self.data[char] = self.data.get(char, 0) + 1

    def __repr__(self):
        output = []
        for key, value in sorted(self.data.items()):
            output.append(f"{key}: {value} time/s")
        return '\n'.join(output)


given_text = CountSymbols(input())
given_text.occurrences()
print(given_text)
