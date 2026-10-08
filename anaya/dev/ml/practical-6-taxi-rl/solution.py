# A52 Dipanshu Ambilkar
"""
Practical 6 - Taxi problem solved with Q-learning (simple version)
The taxi moves on a 5x5 grid, picks up the passenger at one corner
and drops them at another.
Rewards: -1 per step, +20 for a correct drop-off,
-10 for a wrong pick-up or drop-off.
"""
import numpy as np

ROWS, COLS = 5, 5
CORNERS = {"R": (0, 0), "G": (0, 4), "Y": (4, 0), "B": (4, 3)}
ACTIONS = ["up", "down", "left", "right", "pickup", "dropoff"]

def step(state, action):
    taxi, passenger, dest = state          # passenger: corner key or "in_taxi"
    r, c = taxi
    reward, done = -1, False
    if action == "up":
        r = max(0, r - 1)
    elif action == "down":
        r = min(ROWS - 1, r + 1)
    elif action == "left":
        c = max(0, c - 1)
    elif action == "right":
        c = min(COLS - 1, c + 1)
    elif action == "pickup":
        if passenger != "in_taxi" and (r, c) == CORNERS[passenger]:
            passenger = "in_taxi"
        else:
            reward = -10
    elif action == "dropoff":
        if passenger == "in_taxi" and (r, c) == CORNERS[dest]:
            reward, done = 20, True
            passenger = "done"
        else:
            reward = -10
    return ((r, c), passenger, dest), reward, done

def new_episode(rng):
    corners = list(CORNERS)
    start = corners[rng.integers(4)]
    dest = corners[rng.integers(4)]
    while dest == start:
        dest = corners[rng.integers(4)]
    taxi = (rng.integers(ROWS), rng.integers(COLS))
    return (taxi, start, dest)

# Q-learning: a table that stores the value of each action in each state
rng = np.random.default_rng(7)
Q = {}

def q_values(state):
    if state not in Q:
        Q[state] = np.zeros(len(ACTIONS))
    return Q[state]

alpha, gamma, epsilon = 0.1, 0.99, 0.1
for ep in range(2000):
    state = new_episode(rng)
    done = False
    while not done:
        if rng.random() < epsilon:                    # explore
            a = rng.integers(len(ACTIONS))
        else:                                         # exploit best known action
            a = int(np.argmax(q_values(state)))
        next_state, reward, done = step(state, ACTIONS[a])
        best_next = np.max(q_values(next_state))
        q_values(state)[a] += alpha * (reward + gamma * best_next - q_values(state)[a])
        state = next_state
    if (ep + 1) % 500 == 0:
        print(f"Episode {ep + 1} done")

# Test one episode using only the learned (greedy) policy
state = new_episode(rng)
done, total, moves = False, 0, 0
while not done and moves < 100:
    a = int(np.argmax(q_values(state)))
    state, reward, done = step(state, ACTIONS[a])
    total += reward
    moves += 1
print("\nTest episode: total reward =", total, "| moves =", moves)
print("The taxi learned to pick up and drop off correctly."
      if total > 0 else "Still learning - run more episodes.")
