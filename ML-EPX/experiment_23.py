from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1
)

uniform_model = KNeighborsClassifier(n_neighbors=5, weights='uniform').fit(X_train, y_train)
distance_model = KNeighborsClassifier(n_neighbors=5, weights='distance').fit(X_train, y_train)

print(f'Uniform-weighted accuracy: {accuracy_score(y_test, uniform_model.predict(X_test)):.4f}')
print(f'Distance-weighted accuracy: {accuracy_score(y_test, distance_model.predict(X_test)):.4f}')
