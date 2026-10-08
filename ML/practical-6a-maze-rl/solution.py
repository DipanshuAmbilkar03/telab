import numpy as np
from collections import deque
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

r = np.random.default_rng(42)
S, G = (0, 0), (7, 7)
W = {(1, 1), (1, 2), (1, 3), (1, 5), (1, 6), (2, 1), (2, 3), (2, 5),
     (3, 1), (3, 3), (3, 4), (3, 5), (3, 7), (4, 3), (4, 5), (4, 7),
     (5, 0), (5, 1), (5, 3), (5, 5), (5, 7), (6, 5), (6, 7)}
M = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
m = list(M)

def st(p, x):
    a, b = p[0] + M[x][0], p[1] + M[x][1]
    if not (0 <= a < 8 and 0 <= b < 8) or (a, b) in W:
        return p, -5, False
    return ((a, b), 20, True) if (a, b) == G else ((a, b), -1, False)

def bfs():
    q, s = deque([(S, 0)]), {S}
    while q:
        p, d = q.popleft()
        if p == G:
            return d
        for x in m:
            n, _, _ = st(p, x)
            if n not in s and n != p:
                s.add(n)
                q.append((n, d + 1))

print("shortest path (BFS):", bfs())
Q, h = np.zeros((8, 8, 4)), []
for ep in range(2000):
    e, p, dn, tt = max(0.05, 1.0 - ep / 1600.0), S, False, 0
    while not dn:
        w, x = p
        a = r.integers(4) if r.random() < e else int(np.argmax(Q[w, x]))
        n, rw, dn = st(p, m[a])
        Q[w, x, a] += 0.2 * (rw + 0.95 * np.max(Q[n[0], n[1]]) - Q[w, x, a])
        p, tt = n, tt + rw
    h.append(tt)
    if (ep + 1) % 500 == 0:
        print("ep %d avg %.2f" % (ep + 1, np.mean(h[-500:])))
print("training done")
ok, ln = 0, []
for _ in range(100):
    p, ph = S, [S]
    while p != G and len(ph) < 200:
        w, x = p
        p, _, _ = st(p, m[int(np.argmax(Q[w, x]))])
        ph.append(p)
    if ph[-1] == G:
        ok += 1
        ln.append(len(ph) - 1)
print("success rate: %.2f%%" % ok)
print("avg steps:", round(float(np.mean(ln)), 1))
p, ph = S, [S]
while p != G and len(ph) < 200:
    w, x = p
    p, _, _ = st(p, m[int(np.argmax(Q[w, x]))])
    ph.append(p)
plt.figure()
plt.imshow([[1 if (a, b) in W else 0 for b in range(8)] for a in range(8)], cmap="Greys")
plt.plot([q[1] for q in ph], [q[0] for q in ph], color="red", linewidth=2)
plt.plot(S[1], S[0], "go", markersize=10)
plt.plot(G[1], G[0], "bo", markersize=10)
plt.title("maze path")
plt.savefig("maze_path.png")
print("saved maze_path.png")
plt.figure()
plt.plot(np.convolve(h, np.ones(50) / 50, mode="valid"))
plt.xlabel("episode"); plt.ylabel("reward"); plt.title("maze learning curve")
plt.savefig("learning_curve.png")
print("saved learning_curve.png")
g = [["." for _ in range(8)] for _ in range(8)]
for a, b in W:
    g[a][b] = "#"
for a, b in ph[1:-1]:
    g[a][b] = "*"
g[S[0]][S[1]], g[G[0]][G[1]] = "S", "G"
[print(" ".join(row)) for row in g]
