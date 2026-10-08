import numpy as np
from collections import deque
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

SIZE = 8
START = (0, 0)
GOAL = (7, 7)
WALLS = {
    (1, 1), (1, 2), (1, 3), (1, 5), (1, 6),
    (2, 1), (2, 3), (2, 5),
    (3, 1), (3, 3), (3, 4), (3, 5), (3, 7),
    (4, 3), (4, 5), (4, 7),
    (5, 0), (5, 1), (5, 3), (5, 5), (5, 7),
    (6, 5), (6, 7),
}
MOVES = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
moves = list(MOVES)

def step(pos, m):
    r = pos[0] + MOVES[m][0]
    c = pos[1] + MOVES[m][1]
    if not (0 <= r < SIZE and 0 <= c < SIZE) or (r, c) in WALLS:
        return pos, -5, False
    if (r, c) == GOAL:
        return (r, c), 20, True
    return (r, c), -1, False

def bfs():
    q = deque([(START, 0)])
    seen = {START}
    while q:
        pos, d = q.popleft()
        if pos == GOAL:
            return d
        for m in moves:
            npos, _, _ = step(pos, m)
            if npos not in seen and npos != pos:
                seen.add(npos)
                q.append((npos, d + 1))
    return None

print("shortest path (BFS):", bfs())

Q = np.zeros((SIZE, SIZE, 4))
ALPHA, GAMMA = 0.2, 0.95
EPISODES = 2000
hist = []

for ep in range(EPISODES):
    eps = max(0.05, 1.0 - ep / (EPISODES * 0.8))
    pos, done = START, False
    total = 0
    while not done:
        r, c = pos
        if rng.random() < eps:
            a = rng.integers(4)
        else:
            a = int(np.argmax(Q[r, c]))
        npos, reward, done = step(pos, moves[a])
        nr, nc = npos
        Q[r, c, a] += ALPHA * (reward + GAMMA * np.max(Q[nr, nc]) - Q[r, c, a])
        pos, total = npos, total + reward
    hist.append(total)
    if (ep + 1) % 500 == 0:
        print("ep %d avg %.2f" % (ep + 1, np.mean(hist[-500:])))

print("training done")

EVAL = 100
wins, lens = 0, []
for _ in range(EVAL):
    pos, path = START, [START]
    while pos != GOAL and len(path) < 200:
        r, c = pos
        a = int(np.argmax(Q[r, c]))
        pos, _, _ = step(pos, moves[a])
        path.append(pos)
    if path[-1] == GOAL:
        wins += 1
        lens.append(len(path) - 1)

print("success rate: %.2f%%" % (100 * wins / EVAL))
print("avg steps:", round(float(np.mean(lens)), 1))

pos, path = START, [START]
while pos != GOAL and len(path) < 200:
    r, c = pos
    a = int(np.argmax(Q[r, c]))
    pos, _, _ = step(pos, moves[a])
    path.append(pos)

grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]
for r, c in WALLS:
    grid[r][c] = "#"
for r, c in path[1:-1]:
    grid[r][c] = "*"
grid[START[0]][START[1]] = "S"
grid[GOAL[0]][GOAL[1]] = "G"
plt.figure()
plt.imshow([[1 if (r, c) in WALLS else 0 for c in range(SIZE)] for r in range(SIZE)], cmap="Greys")
pr = [p[0] for p in path]
pc = [p[1] for p in path]
plt.plot(pc, pr, color="red", linewidth=2)
plt.plot(START[1], START[0], "go", markersize=10)
plt.plot(GOAL[1], GOAL[0], "bo", markersize=10)
plt.title("maze path")
plt.savefig("maze_path.png")
print("saved maze_path.png")

avg = np.convolve(hist, np.ones(50) / 50, mode="valid")
plt.figure()
plt.plot(avg)
plt.xlabel("episode")
plt.ylabel("reward")
plt.title("maze learning curve")
plt.savefig("learning_curve.png")
print("saved learning_curve.png")

for row in grid:
    print(" ".join(row))
