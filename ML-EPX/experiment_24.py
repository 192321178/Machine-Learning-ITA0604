import numpy as np

def locally_weighted_regression(x_query, X, y, tau=1.0):
    weights = np.exp(-((X - x_query) ** 2) / (2 * tau ** 2))
    design = np.column_stack((np.ones(len(X)), X))
    W = np.diag(weights)
    theta = np.linalg.pinv(design.T @ W @ design) @ design.T @ W @ y
    return np.array([1.0, x_query]) @ theta

X = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([0, 1, 4, 9, 16], dtype=float)
queries = [0.5, 1.5, 2.5]
predictions = [locally_weighted_regression(x, X, y) for x in queries]
print('Sample predictions:', np.round(predictions, 3))
