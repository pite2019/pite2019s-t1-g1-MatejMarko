class Matrix:

    def __init__(self, matrix=None, cols=None, rows=None, value=0):

        if matrix:
            self.data = matrix
        else:
            self.data = list([value for c in range(cols)] for r in range(rows))

        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __add__(self, other):
        return self.add_matrices(other)

    def __radd__(self, other):
        return self.add_matrices(other)

    def __sub__(self, other):
        return self.subtract_matrices(other)

    def __rsub__(self, other):
        return self.subtract_matrices(other, True)

    def __matmul__(self, other):
        return self.multiply(other)

    def add_matrices(self, other):

        new_matrix = Matrix(cols=self.cols, rows=self.cols)
        to_be_added = self.set_other_matrix(other)

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                new_matrix[i][j] = self.data[i][j] + to_be_added.data[i][j]
        return new_matrix

    def subtract_matrices(self, other, r=False):
        new_matrix = Matrix(cols=self.cols, rows=self.cols)
        other_matrix = self.set_other_matrix(other)

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if not r:
                    new_matrix[i][j] = self.data[i][j] - other_matrix.data[i][j]
                else:
                    new_matrix[i][j] = other_matrix.data[i][j] - self.data[i][j]
        return new_matrix

    def set_other_matrix(self, other):
        other_matrix = None

        if isinstance(other, Matrix):
            other_matrix = other
        elif isinstance(other, int):
            other_matrix = Matrix(cols=self.cols, rows=self.rows, value=other)

        return other_matrix

    def multiply(self, other):

        multiplied_matrix = Matrix(rows=self.rows, cols=other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.cols):
                    multiplied_matrix[i][j] += self.data[i][k] * other.data[k][j]

        return multiplied_matrix

    def __str__(self):

        longest_in_each_column = self.get_longest_in_each_column()

        output = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                output += str(add_spaces(len(str(self.data[i][j])), longest_in_each_column[j])) + str(
                    self.data[i][j]) + "  "
            output += "\n"
        return output

    def get_longest_in_each_column(self):
        longest_in_each_column = []
        for i in range(len(self.data[0])):
            longest = 0
            for j in range(len(self.data)):
                if len(str(self.data[j][i])) > longest:
                    longest = len(str(self.data[j][i]))
            longest_in_each_column.append(longest)
        return longest_in_each_column


def add_spaces(length, goal):
    spaces = ""
    for c in range(goal - length):
        spaces += " "
    return spaces
