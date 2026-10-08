# A52 Dipanshu Ambilkar
"""
Practical 4 - K-Means clustering on the Iris dataset (simple version)
Requirement: cluster the data and choose the number of clusters
with the elbow method.
"""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. Load data (we ignore the species labels while clustering)
X, species = load_iris(return_X_y=True)
print("Shape:", X.shape)

# 2. Elbow method: inertia for k = 1..10
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=7)
    km.fit(X)
    inertias.append(km.inertia_)
print("Inertias for k=1..10:", [round(v) for v in inertias])

plt.plot(range(1, 11), inertias, marker="o")
plt.xlabel("k")
plt.ylabel("Inertia")
plt.title("Elbow method")
plt.savefig("elbow.png")
print("Plot saved: elbow.png")

# 3. The elbow is at k=3 (iris has 3 species), so cluster with k=3
km = KMeans(n_clusters=3, n_init=10, random_state=7)
labels = km.fit_predict(X)
print("\nCluster sizes:", [sum(labels == c) for c in range(3)])

# 4. Quick check: how pure are the clusters?
for c in range(3):
    counts = [sum((labels == c) & (species == s)) for s in range(3)]
    print(f"Cluster {c}: species counts {counts}")
