import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])
weights = np.zeros(3)  # bias, w1, w2
learning_rate = 0.1

for _ in range(20):
    for inputs, target in zip(X, y):
        inputs_with_bias = np.insert(inputs, 0, 1)
        prediction = 1 if np.dot(weights, inputs_with_bias) > 0 else 0
        weights += learning_rate * (target - prediction) * inputs_with_bias

print('Learned weights (bias, w1, w2):', weights)
for inputs in X:
    inputs_with_bias = np.insert(inputs, 0, 1)
    prediction = 1 if np.dot(weights, inputs_with_bias) > 0 else 0
    print(f'{inputs.tolist()} -> {prediction}')
