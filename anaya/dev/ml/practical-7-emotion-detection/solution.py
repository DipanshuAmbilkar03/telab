# A52 Dipanshu Ambilkar
"""
Practical 7 - Emotion detection from text (simple version)
Requirements: preprocess text, convert it to TF-IDF features
(unigrams + bigrams), train two classifiers (Logistic Regression and
Naive Bayes), compare them with accuracy, show a confusion matrix,
and test the better model on new unseen sentences.
"""
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Build a labelled dataset from emotion word lists.
#    (Seeded, so it is the same on every run. Templates share vocabulary
#    within each emotion, the way real emotion messages do.)
import numpy as np

rng = np.random.default_rng(7)

EMOTION_WORDS = {
    "happy": ["happy", "joyful", "glad", "wonderful", "excited", "cheerful",
              "delighted", "thrilled", "amazing", "lovely", "great", "fantastic",
              "blissful", "ecstatic", "merry", "jubilant"],
    "sad": ["sad", "gloomy", "depressed", "lonely", "miserable", "sorrowful",
            "heartbroken", "tearful", "down", "hopeless", "blue", "melancholy",
            "dismal", "forlorn", "weepy", "dejected"],
    "angry": ["angry", "furious", "mad", "irritated", "outraged", "livid",
              "enraged", "infuriated", "annoyed", "hostile", "bitter",
              "resentful", "fuming", "seething", "wrathful", "cross"],
}
TEMPLATES = [
    "I feel {w} today",
    "I am so {w} right now",
    "Feeling {w} and {w2} this morning",
    "This makes me feel {w}",
    "I woke up feeling {w}",
    "What a {w} day it has been",
    "I am {w} about everything",
    "Feeling completely {w} and {w2}",
]

texts, labels = [], []
for emotion, words in EMOTION_WORDS.items():
    for _ in range(60):
        t = rng.choice(TEMPLATES)
        w1, w2 = rng.choice(words, 2, replace=False)
        texts.append(t.format(w=w1, w2=w2))
        labels.append(emotion)
print("Dataset size:", len(texts))

# 2. Preprocess: lowercase, remove URLs/mentions/punctuation
def clean(text):
    text = text.lower()
    text = re.sub(r"http\S+|@\w+", "", text)
    text = re.sub(r"[^a-z ]", "", text)
    return text.strip()

texts = [clean(t) for t in texts]
print("Example after cleaning:", texts[0])

# 3. TF-IDF features (single words + word pairs)
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(texts)

# 4. Train both classifiers and compare accuracy
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=7, stratify=labels)

models = {"Logistic Regression": LogisticRegression(max_iter=1000),
          "Naive Bayes": MultinomialNB()}
scores = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    scores[name] = acc
    print(f"{name}: accuracy = {acc:.3f}")

# 5. Confusion matrix of the better model
best = max(scores, key=scores.get)
print("\nConfusion matrix (" + best + "):")
print(confusion_matrix(y_test, models[best].predict(X_test),
                       labels=["happy", "sad", "angry"]))

# 6. Test the better model on brand-new sentences
for sentence in ["I am joyful and thrilled today",
                 "Feeling gloomy and tearful tonight",
                 "That insult made me absolutely furious"]:
    vec = vectorizer.transform([clean(sentence)])
    print(f'"{sentence}" -> {models[best].predict(vec)[0]}')
