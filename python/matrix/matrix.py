class Matrix(object):
    def __init__(self, matrix_string):
        self.data = [[int(n) for n in r.split(' ')] for r in matrix_string.split("\n")]

    def row(self, index):
        return [r for r in self.data[index - 1]]

    def column(self, index):
        return [row[index - 1] for row in self.data]

