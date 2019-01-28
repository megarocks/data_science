
import numpy as np


def naive_add_matrix_and_vector(x, y):
    assert x.ndim == 2
    assert y.ndim == 1
    assert x.shape[1] == y.shape[0]

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.shape)

vector = np.array([
    7, 5, 2
])
print(vector.shape)

sum = naive_add_matrix_and_vector(matrix, vector)
print(sum)
