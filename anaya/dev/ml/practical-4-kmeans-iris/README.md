# Practical 4: K-Means Clustering on the Iris Dataset (simple version)

## Aim
Cluster the iris data with K-Means and choose the number of clusters using the elbow method.

## Problem Statement (from the syllabus)
Implement K-Means clustering on Iris.csv dataset. Determine the number of clusters using the elbow method.

## Steps followed
1. Load the iris dataset (labels hidden from the algorithm).
2. Elbow method: compute inertia for k = 1..10 and plot it (`elbow.png`).
3. The elbow is at k = 3 (iris has 3 species), so cluster with k = 3.
4. Check cluster purity against the true species labels.

## Output
- The inertia curve bends sharply at k = 3; the three clusters line up almost exactly with the three species.
