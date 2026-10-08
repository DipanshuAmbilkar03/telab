import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

LOCS = {"R": (0, 0), "G": (0, 4), "Y": (4, 0), "B": (4, 3)}
NAMES = ["R", "G", "Y", "B"]
WALLS = {(0, 1), (1, 1), (3, 0), (4, 0), (3, 2), (4, 2)}
ACTIONS = ["south", "north", "east", "west", "pickup", "dropoff"]

def encode(row, col, p, d):
    return ((row * 5 + col) * 5 + p) * 4 + d

def decode(s):
    d = s % 4
    s //= 4
    p = s % 5
    s //= 5
    return s // 5, s % 5, p, d

class TaxiEnv:
    def reset(self):
        row, col = rng.integers(0, 5, 2)
        p, d = rng.choice(4, 2, replace=False)
        self.s = (int(row), int(col), int(p), int(d))
        return encode(*self.s)

    def step(self, a):
        row, col, p, d = self.s
        reward, done = -1, False
        if a == 0 and row < 4:
            row += 1
        elif a == 1 and row > 0:
            row -= 1
        elif a == 2 and col < 4 and (row, col) not in WALLS:
            col += 1
        elif a == 3 and col > 0 and (row, col - 1) not in WALLS:
            col -= 1
        elif a == 4:
            if p < 4 and (row, col) == LOCS[NAMES[p]]:
                p = 4
            else:
                reward = -10
        elif a == 5:
            if p == 4 and (row, col) == LOCS[NAMES[d]]:
                done, reward = True, 20
            else:
                reward = -10
        self.s = (row, col, p, d)
        return encode(*self.s), reward, done

env = TaxiEnv()
print("taxi 5x5, 4 locations, 6 actions, 500 states")

Q = np.zeros((500, 6))
ALPHA, GAMMA = 0.5, 0.99
EPISODES, MAX_STEPS = 3000, 200
hist = []

for ep in range(EPISODES):
    eps = max(0.05, 1.0 - ep / (EPISODES * 0.8))
    s = env.reset()
    total = 0
    for _ in range(MAX_STEPS):
        if rng.random() < eps:
            a = rng.integers(6)
        else:
            a = int(np.argmax(Q[s]))
        s2, r, done = env.step(a)
        Q[s, a] += ALPHA * (r + GAMMA * np.max(Q[s2]) - Q[s, a])
        s, total = s2, total + r
        if done:
            break
    hist.append(total)
    if (ep + 1) % 600 == 0:
        print("ep %d eps %.2f avg %.2f" % (ep + 1, eps, np.mean(hist[-600:])))

print("training done")

EVAL = 100
rewards, steps, ok = [], [], 0
for _ in range(EVAL):
    s = env.reset()
    total, st = 0, 0
    for _ in range(MAX_STEPS):
        a = int(np.argmax(Q[s]))
        s, r, done = env.step(a)
        total, st = total + r, st + 1
        if done:
            ok += 1
            break
    rewards.append(total)
    steps.append(st)

print("success rate: %.2f%%" % (100 * ok / EVAL))
print("avg reward: %.2f" % np.mean(rewards))
print("avg steps: %.1f" % np.mean(steps))

avg = np.convolve(hist, np.ones(100) / 100, mode="valid")
plt.figure()
plt.plot(avg)
plt.xlabel("episode")
plt.ylabel("reward")
plt.title("taxi learning curve")
plt.savefig("learning_curve.png")
print("saved learning_curve.png")

print("demo episode:")
s = env.reset()
for i in range(30):
    a = int(np.argmax(Q[s]))
    s, r, done = env.step(a)
    print("step %d action %s reward %d" % (i + 1, ACTIONS[a], r))
    if done:
        print("delivered")
        break
