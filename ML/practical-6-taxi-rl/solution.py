import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

r = np.random.default_rng(42)
L = {"R": (0, 0), "G": (0, 4), "Y": (4, 0), "B": (4, 3)}
N = ["R", "G", "Y", "B"]
W = {(0, 1), (1, 1), (3, 0), (4, 0), (3, 2), (4, 2)}
A = ["south", "north", "east", "west", "pickup", "dropoff"]

def e(w, x, p, d):
    return ((w * 5 + x) * 5 + p) * 4 + d

def f(s):
    d = s % 4; s //= 4; p = s % 5; s //= 5
    return s // 5, s % 5, p, d

class T:
    def rs(self):
        w, x = r.integers(0, 5, 2)
        p, d = r.choice(4, 2, replace=False)
        self.s = (int(w), int(x), int(p), int(d))
        return e(*self.s)
    def st(self, a):
        w, x, p, d = self.s
        rw, dn = -1, False
        if a == 0 and w < 4:
            w += 1
        elif a == 1 and w > 0:
            w -= 1
        elif a == 2 and x < 4 and (w, x) not in W:
            x += 1
        elif a == 3 and x > 0 and (w, x - 1) not in W:
            x -= 1
        elif a == 4:
            p, rw = (4, rw) if p < 4 and (w, x) == L[N[p]] else (p, -10)
        elif a == 5:
            dn, rw = (True, 20) if p == 4 and (w, x) == L[N[d]] else (False, -10)
        self.s = (w, x, p, d)
        return e(*self.s), rw, dn

t = T()
print("taxi 5x5, 4 locations, 6 actions, 500 states")
Q = np.zeros((500, 6))
h = []
for ep in range(3000):
    ep2 = max(0.05, 1.0 - ep / 2400.0)
    s, tt = t.rs(), 0
    for _ in range(200):
        a = r.integers(6) if r.random() < ep2 else int(np.argmax(Q[s]))
        s2, rw, dn = t.st(a)
        Q[s, a] += 0.5 * (rw + 0.99 * np.max(Q[s2]) - Q[s, a])
        s, tt = s2, tt + rw
        if dn:
            break
    h.append(tt)
    if (ep + 1) % 600 == 0:
        print("ep %d eps %.2f avg %.2f" % (ep + 1, ep2, np.mean(h[-600:])))
print("training done")
rw2, st2, ok = [], [], 0
for _ in range(100):
    s, tt, st = t.rs(), 0, 0
    for _ in range(200):
        a = int(np.argmax(Q[s]))
        s, rw, dn = t.st(a)
        tt, st = tt + rw, st + 1
        if dn:
            ok += 1
            break
    rw2.append(tt); st2.append(st)
print("success rate: %.2f%%" % ok)
print("avg reward: %.2f" % np.mean(rw2))
print("avg steps: %.1f" % np.mean(st2))
plt.figure()
plt.plot(np.convolve(h, np.ones(100) / 100, mode="valid"))
plt.xlabel("episode"); plt.ylabel("reward"); plt.title("taxi learning curve")
plt.savefig("learning_curve.png")
print("saved learning_curve.png")
print("demo episode:")
s = t.rs()
for i in range(30):
    a = int(np.argmax(Q[s]))
    s, rw, dn = t.st(a)
    print("step %d action %s reward %d" % (i + 1, A[a], rw))
    if dn:
        print("delivered")
        break
