import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

rng = np.random.default_rng(42)

JOY_T = ["So happy about {t}!", "Feeling joyful because of {t}.", "What a wonderful {t}!",
         "Thrilled beyond words by {t}.", "I am delighted with {t}.",
         "Pure bliss thinking about {t}.", "Over the moon over {t}.",
         "Cheerful all day thanks to {t}."]
ANGER_T = ["Furious about {t}!", "I am so angry at {t}.", "This {t} makes me mad.",
           "Boiling with rage over {t}.", "Livid about {t} right now.",
           "Outraged by {t}.", "I hate {t} so much.", "Seething over {t}."]
SAD_T = ["So sad about {t}.", "Heartbroken over {t}.", "Crying because of {t}.",
         "Feeling gloomy about {t}.", "Tears fall thinking of {t}.",
         "Depressed by {t}.", "Lonely without {t}.", "Miserable about {t}."]
FEAR_T = ["Scared of {t}.", "Terrified by {t}!", "I fear {t} deeply.",
          "Anxious about {t}.", "Trembling at the thought of {t}.",
          "Horrified by {t}.", "Panicking over {t}.", "Dreading {t}."]
SURPRISE_T = ["Wow, {t}!", "Shocked by {t}!", "Amazed at {t}.",
              "Unbelievable {t}!", "Stunned by {t}.", "Astonished at {t}.",
              "Blown away by {t}!", "Caught off guard by {t}."]
LOVE_T = ["I love {t} so much.", "Adore {t} deeply.", "My heart belongs to {t}.",
          "Enchanted by {t}.", "I cherish {t}.", "Devoted to {t}.",
          "Crazy about {t}.", "I treasure {t}."]

JOY_W = ["the news", "my friends", "this morning", "the party", "good grades",
         "the trip", "my family", "the surprise", "the festival", "the gift",
         "the weekend", "the results", "the music", "the game", "my birthday",
         "the promotion", "the holiday", "the concert", "the win", "the call"]
ANGER_W = ["the delay", "the noise", "this traffic", "the rude reply", "the mess",
           "the unfair call", "the long queue", "the broken phone", "the lie",
           "the arrogance", "the spam", "the price hike", "the cheating",
           "the insult", "the slow service", "the betrayal", "the chaos",
           "the mistake", "the ignorance", "the attitude"]
SAD_W = ["the loss", "the goodbye", "the empty house", "the rainy day",
         "the old photos", "the missed chance", "the silence", "the failure",
         "the distance", "the news today", "the lonely night", "the memory",
         "the broken dream", "the farewell", "the dark room", "the letter",
         "the absence", "the regret", "the ending", "the void"]
FEAR_W = ["the dark", "the exam", "the storm", "the injection", "the heights",
          "the interview", "the loud sound", "the spider", "the ghost story",
          "the turbulence", "the operation", "the deadline", "the dog",
          "the horror movie", "the thunder", "the crowd", "the fire alarm",
          "the deep water", "the dentist", "the night walk"]
SURPRISE_W = ["the twist", "the announcement", "the gift", "the visit",
              "the result", "the coincidence", "the discovery", "the prize",
              "the reunion", "the plot twist", "the flash mob", "the proposal",
              "the lottery win", "the comeback", "the reveal", "the record",
              "the magic trick", "the guest", "the fireworks", "the news flash"]
LOVE_W = ["my partner", "my mom", "my dog", "this song", "my best friend",
          "my hometown", "the little things", "my grandma", "this place",
          "my sister", "the ocean", "my cat", "old letters", "my teacher",
          "the mountains", "my brother", "sunsets", "my family", "this book",
          "childhood memories"]

def make_samples(templates, words, n=200):
    combos = [t.format(t=w) for t in templates for w in words]
    idx = rng.permutation(len(combos))[:n]
    out = []
    for j, i in enumerate(idx):
        s = combos[i]
        if j % 40 == 0:
            s = s + " @friend"
        if j % 55 == 0:
            s = s + " https://bit.ly/mood123"
        out.append(s)
    return out

texts = []
labels = []
for emo, t, w in [("joy", JOY_T, JOY_W), ("anger", ANGER_T, ANGER_W),
                  ("sadness", SAD_T, SAD_W), ("fear", FEAR_T, FEAR_W),
                  ("surprise", SURPRISE_T, SURPRISE_W), ("love", LOVE_T, LOVE_W)]:
    s = make_samples(t, w)
    texts += s
    labels += [emo] * len(s)

print("total:", len(texts))

def clean(t):
    t = t.lower()
    t = re.sub(r"http\S+|@\w+", "", t)
    t = re.sub(r"[^a-z ]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

texts = [clean(t) for t in texts]
print("example:", texts[0])

uniq, counts = np.unique(labels, return_counts=True)
plt.figure()
plt.bar(uniq, counts)
plt.title("class distribution")
plt.savefig("class_distribution.png")
print("saved class_distribution.png")

vec = TfidfVectorizer(ngram_range=(1, 2), max_features=3000, stop_words="english")
X = vec.fit_transform(texts)
print("features:", X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42, stratify=labels)

lr = LogisticRegression(max_iter=1000)
nb = MultinomialNB()
lr.fit(X_train, y_train)
nb.fit(X_train, y_train)
acc_lr = accuracy_score(y_test, lr.predict(X_test))
acc_nb = accuracy_score(y_test, nb.predict(X_test))
print("logistic regression:", round(acc_lr, 4))
print("naive bayes:", round(acc_nb, 4))

best = lr if acc_lr >= acc_nb else nb
print(classification_report(y_test, best.predict(X_test)))

cm = confusion_matrix(y_test, best.predict(X_test), labels=["joy", "anger", "sadness", "fear", "surprise", "love"])
plt.figure()
plt.imshow(cm, cmap="Blues")
plt.xticks(range(6), ["joy", "anger", "sadness", "fear", "surprise", "love"], rotation=45)
plt.yticks(range(6), ["joy", "anger", "sadness", "fear", "surprise", "love"])
plt.title("confusion matrix")
plt.colorbar()
plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("saved confusion_matrix.png")

new = [
    "I am so happy and thrilled today",
    "This delay makes me absolutely furious",
    "Feeling gloomy and heartbroken tonight",
    "Terrified of the thunderstorm outside",
    "Wow what an unbelievable surprise",
    "I adore my family more than anything",
    "Cheerful morning full of laughter",
    "Anxious and trembling before the exam",
]
for s in new:
    v = vec.transform([clean(s)])
    print('"%s" -> %s' % (s, best.predict(v)[0]))
