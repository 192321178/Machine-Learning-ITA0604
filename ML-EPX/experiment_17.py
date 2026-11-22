import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.7, random_state=1)
model = GaussianMixture(n_components=3, random_state=1)
model.fit(X)
labels = model.predict(X)
print('Converged:', model.converged_)
print('Number of samples clustered:', len(labels))
