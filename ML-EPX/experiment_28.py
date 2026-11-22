import numpy as np

a = np.arange(12).reshape(3, 4)
print('Array:\n', a)
print('a[1, 2]:', a[1, 2])
print('Column 1:', a[:, 1])
print('Elements greater than 5:', a[a > 5])
a[a % 2 == 0] = 0
print('After zeroing even values:\n', a)
