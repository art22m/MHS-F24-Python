import numpy as np
import random


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        if not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError("invalid dimensions for matrix addition")

        res = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                res[i][j] = self.data[i][j] + other.data[i][j]

        return Matrix(res)

    def __mul__(self, other):
        if not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError("invalid dimensions for matrix multiplication")

        res = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                res[i][j] = self.data[i][j] * other.data[i][j]

        return Matrix(res)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("invalid dimensions for matrix multiplication")

        res = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(res)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


def main():
    random.seed(0)

    data1 = np.random.randint(0, 10, (10, 10))
    mat1 = Matrix(data1.tolist())

    data2 = np.random.randint(0, 10, (10, 10))
    mat2 = Matrix(data2.tolist())

    with open('artifacts/3.1/matrix+.txt', 'w') as f:
        f.write(str(mat1 + mat2))
    with open('artifacts/3.1/matrix*.txt', 'w') as f:
        f.write(str(mat1 * mat2))
    with open('artifacts/3.1/matrix@.txt', 'w') as f:
        f.write(str(mat1 @ mat2))


if __name__ == "__main__":
    main()
