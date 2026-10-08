from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

X, y = fetch_openml(name="car", version=1, return_X_y=True, as_frame=True)
print(X.shape, sorted(y.unique()))

X = OrdinalEncoder().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred))
