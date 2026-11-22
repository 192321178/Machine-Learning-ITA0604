import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
np.save('array.npy', a)
np.savetxt('array.csv', a, delimiter=',', fmt='%d')

loaded_npy = np.load('array.npy')
loaded_csv = np.loadtxt('array.csv', delimiter=',', dtype=int)
print('Loaded from NPY:\n', loaded_npy)
print('Loaded from CSV:\n', loaded_csv)
