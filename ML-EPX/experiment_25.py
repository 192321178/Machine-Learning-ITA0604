import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0])
centres = X.copy()
sigma = 0.5

def rbf_transform(data, centres, width):
    return np.array([
        [np.exp(-np.sum((sample - centre) ** 2) / (2 * width ** 2))
         for centre in centres]
        for sample in data
    ])

X_rbf = rbf_transform(X, centres, sigma)
model = LogisticRegression(C=1000, solver='lbfgs', random_state=0)
model.fit(X_rbf, y)
predictions = model.predict(X_rbf)
print('Predictions:', predictions)
print('Correctly classified:', int(np.sum(predictions == y)), 'of', len(y))
