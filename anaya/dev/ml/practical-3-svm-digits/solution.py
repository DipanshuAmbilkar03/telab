# A52 Dipanshu Ambilkar
"""
Practical 3 - SVM classification of handwritten digits (simple version)
Requirement: classify digit images (0-9) with a Support Vector Machine.
"""
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load the digits dataset (1797 images, 8x8 pixels each)
X, y = load_digits(return_X_y=True)
print("Shape:", X.shape, "| classes:", sorted(set(y)))

# 2. Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# 3. Train an SVM classifier
model = SVC()
model.fit(X_train, y_train)

# 4. Evaluate
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print("\nClassification report:")
print(classification_report(y_test, pred))
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
