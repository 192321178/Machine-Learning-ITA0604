import numpy as np
from sklearn.neighbors import KNeighborsRegressor

X_train = np.array([[0], [1], [2], [3], [4]], dtype=float)
y_train = np.array([0, 2, 4, 6, 8], dtype=float)
X_query = np.array([[1.5], [2.5]])

model = KNeighborsRegressor(n_neighbors=2)
model.fit(X_train, y_train)
predictions = model.predict(X_query)
print('Predictions:', predictions)
