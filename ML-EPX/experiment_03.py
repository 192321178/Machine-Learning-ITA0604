from collections import Counter
from math import log2

# Classic 14-row PlayTennis dataset.
data = [
    ('Sunny', 'Hot', 'High', 'Weak', 'No'), ('Sunny', 'Hot', 'High', 'Strong', 'No'),
    ('Overcast', 'Hot', 'High', 'Weak', 'Yes'), ('Rain', 'Mild', 'High', 'Weak', 'Yes'),
    ('Rain', 'Cool', 'Normal', 'Weak', 'Yes'), ('Rain', 'Cool', 'Normal', 'Strong', 'No'),
    ('Overcast', 'Cool', 'Normal', 'Strong', 'Yes'), ('Sunny', 'Mild', 'High', 'Weak', 'No'),
    ('Sunny', 'Cool', 'Normal', 'Weak', 'Yes'), ('Rain', 'Mild', 'Normal', 'Weak', 'Yes'),
    ('Sunny', 'Mild', 'Normal', 'Strong', 'Yes'), ('Overcast', 'Mild', 'High', 'Strong', 'Yes'),
    ('Overcast', 'Hot', 'Normal', 'Weak', 'Yes'), ('Rain', 'Mild', 'High', 'Strong', 'No'),
]
attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
target_index = 4

def entropy(rows):
    counts = Counter(row[target_index] for row in rows)
    total = len(rows)
    return -sum((n / total) * log2(n / total) for n in counts.values())

def information_gain(rows, attr_index):
    base = entropy(rows)
    values = sorted({row[attr_index] for row in rows})
    remainder = 0.0
    for value in values:
        subset = [row for row in rows if row[attr_index] == value]
        remainder += (len(subset) / len(rows)) * entropy(subset)
    return base - remainder

def id3(rows, attrs):
    labels = [row[target_index] for row in rows]
    if len(set(labels)) == 1:
        return labels[0]
    if not attrs:
        return Counter(labels).most_common(1)[0][0]
    best = max(attrs, key=lambda a: information_gain(rows, attributes.index(a)))
    tree = {best: {}}
    for value in sorted({row[attributes.index(best)] for row in rows}):
        subset = [row for row in rows if row[attributes.index(best)] == value]
        remaining = [a for a in attrs if a != best]
        tree[best][value] = id3(subset, remaining)
    return tree

def predict(tree, sample):
    if isinstance(tree, str):
        return tree
    attribute = next(iter(tree))
    value = sample[attribute]
    branch = tree[attribute].get(value)
    return 'Unknown' if branch is None else predict(branch, sample)

tree = id3(data, attributes)
sample = {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'}
print('Root attribute:', next(iter(tree)))
print('Predicted class:', predict(tree, sample))
