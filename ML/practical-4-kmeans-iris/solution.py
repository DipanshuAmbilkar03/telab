import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)
print(X.shape)
v = [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_ for k in range(1, 11)]
print([round(i) for i in v])
plt.plot(range(1, 11), v, marker="o")
plt.xlabel("k"); plt.ylabel("inertia"); plt.title("elbow")
plt.savefig("elbow.png")
print("saved elbow.png")
l = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X)
print("cluster sizes:", [int(np.sum(l == i)) for i in range(3)])
[print("cluster", i, [int(np.sum((l == i) & (y == j))) for j in range(3)]) for i in range(3)]
