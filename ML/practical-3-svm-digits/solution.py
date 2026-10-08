from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X, y = load_digits(return_X_y=True)
print(X.shape)
a, b, c, d = train_test_split(X, y, test_size=0.2, random_state=42)
m = SVC().fit(a, c)
p = m.predict(b)
print("accuracy:", round(accuracy_score(d, p), 4))
print(classification_report(d, p))
print(confusion_matrix(d, p))
