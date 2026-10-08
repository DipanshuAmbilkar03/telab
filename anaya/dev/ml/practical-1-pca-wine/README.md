# Practical 1: PCA on the Wine Dataset (simple version)

## Aim
Apply PCA for dimensionality reduction on the wine dataset and inspect whether the wine groups separate using a small number of principal components.

## Problem Statement (from the syllabus)
Use the PCA algorithm on a dataset of wine measurements (alcohol, ash, magnesium, ...). Transform the data so that most variation is captured by a small number of principal components, making it easier to distinguish the wine groups by inspecting these components.
Dataset: https://media.geeksforgeeks.org/wp-content/uploads/Wine.csv

## Steps followed
1. Load the wine CSV from the syllabus link (178 rows, 13 measurements, Customer_Segment label).
2. Standardize the features with StandardScaler (PCA is scale-sensitive).
3. Fit PCA with 2 components and check the explained variance ratio.
4. Draw a scatter plot of PC1 vs PC2 coloured by wine segment.

## Output
- 2 components keep ~55-60% of the total variance; the three segments form visibly separated groups in the plot.
- Plot saved as `pca_wine.png`.
