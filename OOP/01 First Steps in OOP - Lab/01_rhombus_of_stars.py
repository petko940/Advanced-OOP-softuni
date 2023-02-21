class Rhombus:
    def __init__(self, size):
        self.size = size

    def draw(self):
        output = []
        for row in range(1, self.size + 1):
            if row == 1:
                output.append((self.size - row) * " " + row * "*")
            else:
                output.append((self.size - row) * " " + row * "* ")

        for rows in range(0, self.size - 1):
            if rows == 0:
                output.append((self.size - (row - 1)) * " " + (self.size - 1) * "* ")
            else:
                output.append((rows + 1) * " " + (self.size - rows - 1) * "* ")
        return '\n'.join(output)


r = Rhombus(int(input()))
print(r.draw())
