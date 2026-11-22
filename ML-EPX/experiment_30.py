import numpy as np

rng = np.random.default_rng(42)
np.set_printoptions(precision=3, suppress=True)
uniform = rng.random((2, 3))
integers = rng.integers(0, 10, size=5)
gaussian = rng.normal(0, 1, size=5)
print('Uniform random 2x3:\n', uniform)
print('Random integers:', integers)
print('Gaussian samples:', gaussian)

n = 100000
points = rng.random((n, 2))
inside = np.sum(points[:, 0] ** 2 + points[:, 1] ** 2 <= 1)
print(f'Estimated pi: {4 * inside / n:.5f}')
