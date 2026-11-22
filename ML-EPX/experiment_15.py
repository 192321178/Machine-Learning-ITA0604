from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

messages = [
    'win a free prize now', 'claim your free cash prize',
    'limited offer win money', 'free entry in contest',
    'urgent claim your reward', 'meeting scheduled for tomorrow',
    'please send the project report', 'are we meeting today',
    'lunch at noon', 'your assignment is ready',
    'win cash now', 'project meeting tomorrow',
    'free prize claim now', 'please call me later',
    'urgent free offer'
]
labels = [
    'spam', 'spam', 'spam', 'spam', 'spam',
    'ham', 'ham', 'ham', 'ham', 'ham',
    'spam', 'ham', 'spam', 'ham', 'spam'
]

X_train, X_test, y_train, y_test = train_test_split(
    messages, labels, test_size=0.20, random_state=1, stratify=labels
)
vectorizer = CountVectorizer().fit(X_train)
X_train_vec = vectorizer.transform(X_train)
X_test_vec = vectorizer.transform(X_test)
model = MultinomialNB().fit(X_train_vec, y_train)
predictions = model.predict(X_test_vec)
print(f'Accuracy: {accuracy_score(y_test, predictions):.2f}')
print('Confusion matrix (ham, spam):')
print(confusion_matrix(y_test, predictions, labels=['ham', 'spam']))
