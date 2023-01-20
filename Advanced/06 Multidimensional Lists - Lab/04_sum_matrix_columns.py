class SumMatrixColumns:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

    def fill_matrix(self):
        self.matrix = [[int(x) for x in input().split()] for row in range(self.rows)]

    def output(self):
        output = []
        for col in range(self.columns):
            sum = 0
            for row in range(self.rows):
                sum += self.matrix[row][col]
            print(sum)


rows, columns = [int(x) for x in input().split(", ")]
sum_matrix = SumMatrixColumns(rows, columns)
sum_matrix.fill_matrix()
sum_matrix.output()
