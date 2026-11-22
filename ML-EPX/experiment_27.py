import numpy as np

np.set_printoptions(precision=3, suppress=True)
a = np.array([1, 2, 3, 4])
zeros = np.zeros((2, 3), dtype=int)
steps = np.arange(0, 10, 2)
points = np.linspace(0, 1, 5)
print('a:', a, 'shape:', a.shape, 'dimensions:', a.ndim)
print('zeros:\n', zeros)
print('arange:', steps)
print('linspace:', points)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print('x + y:', x + y)
print('x * y:', x * y)
print('dot product:', np.dot(x, y))
print('sqrt(x):', np.sqrt(x))
print('exp(x):', np.exp(x))
