import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

d = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/Wine.csv")
print(d.shape)
print(d["Customer_Segment"].value_counts().sort_index())
print(d.describe().round(2))
X = StandardScaler().fit_transform(d.drop("Customer_Segment", axis=1).values)
y = d["Customer_Segment"].values
p = PCA().fit(X)
e, c = p.explained_variance_ratio_, np.cumsum(p.explained_variance_ratio_)
[print("PC%d %.4f cum %.4f" % (i + 1, e[i], c[i])) for i in range(6)]
print("components for 95 percent:", int(np.argmax(c >= 0.95) + 1))
q = PCA(n_components=2)
Z = q.fit_transform(X)
print("reduced shape:", Z.shape)
print("variance of 2 comps:", round(float(q.explained_variance_ratio_.sum()), 4))
L = pd.DataFrame(q.components_.T, index=d.drop("Customer_Segment", axis=1).columns, columns=["PC1", "PC2"])
print(L["PC1"].abs().sort_values(ascending=False).head(4))
print(L["PC2"].abs().sort_values(ascending=False).head(4))
cc = {1: "red", 2: "green", 3: "blue"}
plt.figure()
[plt.scatter(Z[y == s][:, 0], Z[y == s][:, 1], c=cc[s], label="seg %d" % s) for s in [1, 2, 3]]
plt.xlabel("PC1"); plt.ylabel("PC2"); plt.title("PCA wine"); plt.legend()
plt.savefig("pca_wine.png")
print("saved pca_wine.png")
print("knn accuracy on 2 pcs:", round(float(cross_val_score(KNeighborsClassifier(n_neighbors=5), Z, y, cv=5).mean()), 4))
