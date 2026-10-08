# A52 Dipanshu Ambilkar
"""
Practical 5 - Random Forest to predict car safety (simple version)
Requirement: predict the safety of a car from its features.
"""
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the car evaluation dataset (all features are categories)
X, y = fetch_openml(name="car", version=1, return_X_y=True, as_frame=True)
print("Shape:", X.shape, "| safety classes:", sorted(y.unique()))

# 2. Convert text categories to numbers
X = OrdinalEncoder().fit_transform(X)

# 3. Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# 4. Train a Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=7)
model.fit(X_train, y_train)

# 5. Evaluate
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print("\nClassification report:")
print(classification_report(y_test, pred))
