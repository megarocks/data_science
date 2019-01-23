from numpy import array

a = array(12)
print(a.ndim)  # scalar

b = array([1, 3, 5, 8])
print(b.ndim)  # vector

c = array([
    [1, 3, 5],
    [1, 3, 5],
    [1, 3, 5],
])

print(c.ndim)  # matrix

d = array([
    [[1, 3, 5],
     [1, 3, 5],
     [1, 3, 5], ],
    [[1, 3, 5],
     [1, 3, 5],
     [1, 3, 5], ],
    [[1, 3, 5],
     [1, 3, 5],
     [1, 3, 5], ],
])

print(d.ndim)  # cube
