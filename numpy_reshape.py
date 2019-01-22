from numpy import array

a = array([
    [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],
    [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]],
])

print(a.shape)

print(a)

a = a.reshape(2, 4*4)

print(a)
