import numpy as np

data = np.array([2, 4, 4, 4, 5, 5, 7, 9], dtype=float)
mle_mean = np.mean(data)
mle_variance = np.var(data)  # Population variance: divide by N.
candidates = np.arange(0, 11, dtype=float)
sse = [np.sum((data - candidate) ** 2) for candidate in candidates]
best_candidate = candidates[int(np.argmin(sse))]

print(f'MLE mean: {mle_mean:.2f}')
print(f'MLE variance: {mle_variance:.2f}')
print(f'Candidate minimising SSE: {best_candidate:.0f}')
