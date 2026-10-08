import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)
print(X.shape)

inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X)
    inertias.append(km.inertia_)
print([round(v) for v in inertias])

plt.plot(range(1, 11), inertias, marker="o")
plt.xlabel("k")
plt.ylabel("inertia")
plt.title("elbow")
plt.savefig("elbow.png")
print("saved elbow.png")

km = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = km.fit_predict(X)
print("cluster sizes:", [int(np.sum(labels == i)) for i in range(3)])
for i in range(3):
    print("cluster", i, [int(np.sum((labels == i) & (y == j))) for j in range(3)])
