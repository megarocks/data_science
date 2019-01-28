import numpy as np
from numpy import array

# keras.layers.Dense(512, activation='relu')
# is equal to:
# output = relu(dot(W, input) + b)

# relu is equal to max(x, 0) - rectified linear unit


def naive_relu(x):
    assert len(x.shape) == 2
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x


# tensor = array([
#     [[1, 2, 3], [3, 2, 8], [5, 1, 7], [8, 4, 2], [13, 21, 18]],
#     [[1, 7, 4], [3, 5, 7, ], [11, 34, 18], [5, 1, 7], [3, 2, 8]]
# ])

input_tensor = array([
    [5, 9, -1, 7],
    [1, 8, 5, 4]
])
print(input_tensor)

output_tensor = naive_relu(input_tensor)
print(output_tensor)

z = np.maximum(input_tensor, 0.)  # rely on BLAS implememntation

print(z)
