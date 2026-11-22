import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.30, random_state=1
)
model = DecisionTreeClassifier(criterion='entropy', random_state=1)
model.fit(X_train, y_train)
print(f'Accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}')

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True)
plt.tight_layout()
plt.savefig('iris_tree.png', dpi=150)
print('Decision tree saved as iris_tree.png')
