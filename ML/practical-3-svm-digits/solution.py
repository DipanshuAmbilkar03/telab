from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X, y = load_digits(return_X_y=True)
print(X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
