import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris(as_frame=True)
df = iris.frame.dropna().copy()
X = df[iris.feature_names]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1
)
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
predictions = model.predict(X_test)
print(f'Pipeline accuracy: {accuracy_score(y_test, predictions):.4f}')
print('First five predicted species:', iris.target_names[predictions[:5]])
