# Practical 5: Random Forest for Car Safety Prediction (simple version)

## Aim
Predict the safety of a car from its features using a Random Forest classifier.

## Problem Statement (from the syllabus)
Implement Random Forest Classifier model to predict the safety of the car.
Dataset: https://www.kaggle.com/datasets/elikplim/car-evaluation-data-set (loaded here via sklearn's fetch_openml, no login needed).

## Steps followed
1. Load the car evaluation dataset (1728 rows, all categorical features).
2. Encode the text categories to numbers with OrdinalEncoder.
3. Split into train (80%) and test (20%).
4. Train a Random Forest (100 trees) and evaluate with accuracy and classification report.

## Output
- Accuracy around 95%+ on the test set; the classification report shows per-class precision, recall and F1.
