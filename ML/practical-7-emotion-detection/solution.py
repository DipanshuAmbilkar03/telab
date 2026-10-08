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

r = np.random.default_rng(42)
D = {
 "joy": (["So happy about {t}!", "Feeling joyful because of {t}.", "What a wonderful {t}!",
          "Thrilled beyond words by {t}.", "I am delighted with {t}.",
          "Pure bliss thinking about {t}.", "Over the moon over {t}.",
          "Cheerful all day thanks to {t}."],
         ["the news", "my friends", "this morning", "the party", "good grades",
          "the trip", "my family", "the surprise", "the festival", "the gift",
          "the weekend", "the results", "the music", "the game", "my birthday",
          "the promotion", "the holiday", "the concert", "the win", "the call"]),
 "anger": (["Furious about {t}!", "I am so angry at {t}.", "This {t} makes me mad.",
            "Boiling with rage over {t}.", "Livid about {t} right now.",
            "Outraged by {t}.", "I hate {t} so much.", "Seething over {t}."],
           ["the delay", "the noise", "this traffic", "the rude reply", "the mess",
            "the unfair call", "the long queue", "the broken phone", "the lie",
            "the arrogance", "the spam", "the price hike", "the cheating",
            "the insult", "the slow service", "the betrayal", "the chaos",
            "the mistake", "the ignorance", "the attitude"]),
 "sadness": (["So sad about {t}.", "Heartbroken over {t}.", "Crying because of {t}.",
              "Feeling gloomy about {t}.", "Tears fall thinking of {t}.",
              "Depressed by {t}.", "Lonely without {t}.", "Miserable about {t}."],
             ["the loss", "the goodbye", "the empty house", "the rainy day",
              "the old photos", "the missed chance", "the silence", "the failure",
              "the distance", "the news today", "the lonely night", "the memory",
              "the broken dream", "the farewell", "the dark room", "the letter",
              "the absence", "the regret", "the ending", "the void"]),
 "fear": (["Scared of {t}.", "Terrified by {t}!", "I fear {t} deeply.",
           "Anxious about {t}.", "Trembling at the thought of {t}.",
           "Horrified by {t}.", "Panicking over {t}.", "Dreading {t}."],
          ["the dark", "the exam", "the storm", "the injection", "the heights",
           "the interview", "the loud sound", "the spider", "the ghost story",
           "the turbulence", "the operation", "the deadline", "the dog",
           "the horror movie", "the thunder", "the crowd", "the fire alarm",
           "the deep water", "the dentist", "the night walk"]),
 "surprise": (["Wow, {t}!", "Shocked by {t}!", "Amazed at {t}.",
               "Unbelievable {t}!", "Stunned by {t}.", "Astonished at {t}.",
               "Blown away by {t}!", "Caught off guard by {t}."],
              ["the twist", "the announcement", "the gift", "the visit",
               "the result", "the coincidence", "the discovery", "the prize",
               "the reunion", "the plot twist", "the flash mob", "the proposal",
               "the lottery win", "the comeback", "the reveal", "the record",
               "the magic trick", "the guest", "the fireworks", "the news flash"]),
 "love": (["I love {t} so much.", "Adore {t} deeply.", "My heart belongs to {t}.",
           "Enchanted by {t}.", "I cherish {t}.", "Devoted to {t}.",
           "Crazy about {t}.", "I treasure {t}."],
          ["my partner", "my mom", "my dog", "this song", "my best friend",
           "my hometown", "the little things", "my grandma", "this place",
           "my sister", "the ocean", "my cat", "old letters", "my teacher",
           "the mountains", "my brother", "sunsets", "my family", "this book",
           "childhood memories"]),
}

def mk(t, w, n=200):
    c = [x.format(t=y) for x in t for y in w]
    o = []
    for j, i in enumerate(r.permutation(len(c))[:n]):
        s = c[i]
        s = s + " @friend" if j % 40 == 0 else s
        s = s + " https://bit.ly/mood123" if j % 55 == 0 else s
        o.append(s)
    return o

x, y = [], []
for k, (t, w) in D.items():
    s = mk(t, w)
    x += s
    y += [k] * len(s)
print("total:", len(x))
x = [re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", re.sub(r"http\S+|@\w+", "", t.lower()))).strip() for t in x]
print("example:", x[0])
u, z = np.unique(y, return_counts=True)
plt.figure(); plt.bar(u, z); plt.title("class distribution")
plt.savefig("class_distribution.png")
print("saved class_distribution.png")
v = TfidfVectorizer(ngram_range=(1, 2), max_features=3000, stop_words="english")
X = v.fit_transform(x)
print("features:", X.shape)
a, b, c, d = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
m1, m2 = LogisticRegression(max_iter=1000).fit(a, c), MultinomialNB().fit(a, c)
s1, s2 = accuracy_score(d, m1.predict(b)), accuracy_score(d, m2.predict(b))
print("logistic regression:", round(s1, 4))
print("naive bayes:", round(s2, 4))
m = m1 if s1 >= s2 else m2
print(classification_report(d, m.predict(b)))
lb = ["joy", "anger", "sadness", "fear", "surprise", "love"]
cm = confusion_matrix(d, m.predict(b), labels=lb)
plt.figure(); plt.imshow(cm, cmap="Blues")
plt.xticks(range(6), lb, rotation=45); plt.yticks(range(6), lb)
plt.title("confusion matrix"); plt.colorbar(); plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("saved confusion_matrix.png")
for s in ["I am so happy and thrilled today",
          "This delay makes me absolutely furious",
          "Feeling gloomy and heartbroken tonight",
          "Terrified of the thunderstorm outside",
          "Wow what an unbelievable surprise",
          "I adore my family more than anything",
          "Cheerful morning full of laughter",
          "Anxious and trembling before the exam"]:
    print('"%s" -> %s' % (s, m.predict(v.transform([re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", re.sub(r"http\S+|@\w+", "", s.lower()))).strip()]))[0]))
