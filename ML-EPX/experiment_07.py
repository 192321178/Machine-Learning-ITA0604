import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(output):
    return output * (1 - output)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)
np.random.seed(1)
w1 = np.random.uniform(-1, 1, (2, 4))
w2 = np.random.uniform(-1, 1, (4, 1))

for _ in range(10000):
    hidden = sigmoid(X @ w1)
    output = sigmoid(hidden @ w2)
    output_error = (y - output) * sigmoid_derivative(output)
    hidden_error = (output_error @ w2.T) * sigmoid_derivative(hidden)
    w2 += hidden.T @ output_error * 0.5
    w1 += X.T @ hidden_error * 0.5

print('Predicted output after training:')
print(np.round(output, 3))
