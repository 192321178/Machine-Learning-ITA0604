from itertools import product

X = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change'],
]
y = ['Yes', 'Yes', 'No', 'Yes']

# Each attribute may be one of its observed values or '?'.
domains = [sorted({row[j] for row in X}) for j in range(len(X[0]))]
hypotheses = list(product(*[values + ['?'] for values in domains]))

def covers(h, example):
    return all(a == '?' or a == value for a, value in zip(h, example))

def more_general(h1, h2):
    return all(a == '?' or a == b for a, b in zip(h1, h2))

consistent = [
    h for h in hypotheses
    if all(covers(h, example) == (label == 'Yes') for example, label in zip(X, y))
]

# S: no strictly more-specific consistent hypothesis exists.
S = [h for h in consistent if not any(h2 != h and more_general(h, h2) for h2 in consistent)]
# G: no strictly more-general consistent hypothesis exists.
G = [h for h in consistent if not any(h2 != h and more_general(h2, h) for h2 in consistent)]

print('Final S:', [list(h) for h in S])
print('Final G:', [list(h) for h in G])
