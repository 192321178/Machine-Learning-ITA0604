from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score, f1_score)

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1
)
model = DecisionTreeClassifier(random_state=1).fit(X_train, y_train)
predictions = model.predict(X_test)

print('Confusion matrix:')
print(confusion_matrix(y_test, predictions))
print(f'Accuracy: {accuracy_score(y_test, predictions):.4f}')
print(f'Precision (macro): {precision_score(y_test, predictions, average="macro"):.4f}')
print(f'Recall (macro): {recall_score(y_test, predictions, average="macro"):.4f}')
print(f'F1-score (macro): {f1_score(y_test, predictions, average="macro"):.4f}')
