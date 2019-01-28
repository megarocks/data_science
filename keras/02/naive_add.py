from numpy import array

tensor_x = array([
    [5, 9, -1, 7],
    [1, 8, 5, 4]
])

tensor_y = array([
    [0, 2, 5, 4],
    [5, 2, 8, 7]
])


def naive_add(x, y):
    assert x.ndim == 2
    assert x.ndim == y.ndim
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x


tensor_z = naive_add(tensor_x, tensor_y)
print(tensor_z)

tensor_z_np = tensor_x + tensor_y  # rely on BLAS implememntation
print(tensor_z_np)
