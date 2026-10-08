# A52 Dipanshu Ambilkar
"""
Practical 6a - Maze solved with Q-learning (simple version)
8x8 grid with walls, start (0,0), goal (7,7).
Rewards: -1 per step, +20 for reaching the goal, -5 for hitting a wall.
"""
import numpy as np

SIZE = 8
START, GOAL = (0, 0), (7, 7)
WALLS = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
         (5, 4), (5, 5), (4, 5), (3, 5), (3, 4), (6, 1), (6, 2)}
MOVES = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
moves = list(MOVES)

def step(pos, move):
    r, c = pos[0] + MOVES[move][0], pos[1] + MOVES[move][1]
    if not (0 <= r < SIZE and 0 <= c < SIZE) or (r, c) in WALLS:
        return pos, -5, False          # bumped into a wall
    if (r, c) == GOAL:
        return (r, c), 20, True       # reached the goal
    return (r, c), -1, False          # normal step

# Q-learning: Q[row][col][action] = expected future reward
rng = np.random.default_rng(7)
Q = np.zeros((SIZE, SIZE, 4))
alpha, gamma, epsilon = 0.2, 0.95, 0.15

for ep in range(1500):
    pos, done = START, False
    while not done:
        r, c = pos
        if rng.random() < epsilon:                    # explore
            a = rng.integers(4)
        else:                                         # exploit best known move
            a = int(np.argmax(Q[r, c]))
        npos, reward, done = step(pos, moves[a])
        nr, nc = npos
        Q[r, c, a] += alpha * (reward + gamma * np.max(Q[nr, nc]) - Q[r, c, a])
        pos = npos

# Walk the learned path greedily
pos, path = START, [START]
while pos != GOAL and len(path) < 100:
    r, c = pos
    a = int(np.argmax(Q[r, c]))
    pos, _, _ = step(pos, moves[a])
    path.append(pos)

print("Path length:", len(path) - 1)
print("Reached goal:", path[-1] == GOAL)

# Draw the maze with the learned path (*)
grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]
for (r, c) in WALLS:
    grid[r][c] = "#"
for (r, c) in path[1:-1]:
    grid[r][c] = "*"
grid[START[0]][START[1]] = "S"
grid[GOAL[0]][GOAL[1]] = "G"
print("\nMaze (S=start, G=goal, #=wall, *=path):")
for row in grid:
    print(" ".join(row))
