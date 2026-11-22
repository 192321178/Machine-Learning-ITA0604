import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

X = np.array([
    [-2, 0], [-1, 1], [-1, -1], [0, 1],
    [1, 0], [1, 1], [2, 0], [2, 1]
], dtype=float)
y = (X[:, 0] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1, stratify=y
)
model = Perceptron(max_iter=1000, eta0=0.1, tol=1e-3, random_state=1)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f'Test accuracy: {accuracy_score(y_test, predictions):.2f}')
print('Predictions:', predictions)
