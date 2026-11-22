import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print('Mean:', a.mean())
print('Sum along columns:', a.sum(axis=0))
print('Sum along rows:', a.sum(axis=1))
print(f'Standard deviation: {a.std():.3f}')
print('Minimum per row:', a.min(axis=1))
print('Maximum overall:', a.max())
