import numpy as np
import random


class HashMixin:
    def hash(self):
        return sum(sum(row) for row in self.data)


mult_cache = {}


class Matrix(HashMixin):
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

        key = (self.hash(), other.hash())
        if key in mult_cache:
            return mult_cache[key]

        res = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res[i][j] += self.data[i][k] * other.data[k][j]

        res_matrix = Matrix(res)
        mult_cache[key] = res_matrix
        return res_matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


def collision():
    while True:
        a = Matrix(np.random.randint(0, 100, (2, 2)).tolist())
        c = Matrix(np.random.randint(0, 100, (2, 2)).tolist())
        b = Matrix(np.random.randint(0, 100, (2, 2)).tolist())
        d = Matrix([row[:] for row in b.data])

        if a.hash() == c.hash() and a.data != c.data and b.data == d.data and (a @ b).data != (c @ d).data:
            return a, b, c, d


def main():
    random.seed(0)

    a, b, c, d = collision()
    ab = a @ b
    cd = c @ d

    with open('artifacts/3.3/A.txt', 'w') as f:
        f.write(str(a))
    with open('artifacts/3.3/B.txt', 'w') as f:
        f.write(str(b))
    with open('artifacts/3.3/C.txt', 'w') as f:
        f.write(str(c))
    with open('artifacts/3.3/D.txt', 'w') as f:
        f.write(str(d))
    with open('artifacts/3.3/AB.txt', 'w') as f:
        f.write(str(ab))
    with open('artifacts/3.3/CD.txt', 'w') as f:
        f.write(str(cd))
    with open('artifacts/3.3/hash.txt', 'w') as f:
        f.write(f"AB hash: {ab.hash()}\n")
        f.write(f"CD hash: {cd.hash()}\n")


if __name__ == "__main__":
    main()
