import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

url = "https://media.geeksforgeeks.org/wp-content/uploads/Wine.csv"
df = pd.read_csv(url)

print(df.shape)
print(df["Customer_Segment"].value_counts().sort_index())
print(df.describe().round(2))

X = df.drop("Customer_Segment", axis=1).values
y = df["Customer_Segment"].values

scaler = StandardScaler()
Xs = scaler.fit_transform(X)

pca = PCA()
pca.fit(Xs)
evr = pca.explained_variance_ratio_
cum = np.cumsum(evr)
for i in range(6):
    print("PC%d %.4f cum %.4f" % (i + 1, evr[i], cum[i]))
n = int(np.argmax(cum >= 0.95) + 1)
print("components for 95 percent:", n)

pca2 = PCA(n_components=2)
X2 = pca2.fit_transform(Xs)
print("reduced shape:", X2.shape)
print("variance of 2 comps:", round(float(pca2.explained_variance_ratio_.sum()), 4))

loadings = pd.DataFrame(pca2.components_.T, index=df.drop("Customer_Segment", axis=1).columns, columns=["PC1", "PC2"])
print(loadings["PC1"].abs().sort_values(ascending=False).head(4))
print(loadings["PC2"].abs().sort_values(ascending=False).head(4))

colors = {1: "red", 2: "green", 3: "blue"}
plt.figure()
for s in [1, 2, 3]:
    pts = X2[y == s]
    plt.scatter(pts[:, 0], pts[:, 1], c=colors[s], label="seg %d" % s)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA wine")
plt.legend()
plt.savefig("pca_wine.png")
print("saved pca_wine.png")

scores = cross_val_score(KNeighborsClassifier(n_neighbors=5), X2, y, cv=5)
print("knn accuracy on 2 pcs:", round(float(scores.mean()), 4))
