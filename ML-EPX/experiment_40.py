import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print('Dataset rows:', len(df))
print('Dataset columns:', len(df.columns))

X_train, X_test, y_train, y_test = train_test_split(
    df.iloc[:, :-1], df['target'], test_size=0.30, random_state=1
)
models = {
    'Decision Tree': DecisionTreeClassifier(random_state=1),
    'KNN (k=5)': KNeighborsClassifier(n_neighbors=5)
}
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    results[name] = accuracy_score(y_test, model.predict(X_test))

for name, score in results.items():
    print(f'{name}: {score:.4f}')
plt.bar(results.keys(), results.values())
plt.ylabel('Accuracy')
plt.title('Model Comparison - Iris Dataset')
plt.tight_layout()
plt.savefig('model_comparison.png', dpi=150)
print('Chart saved as model_comparison.png')
