# Practical 6a: Maze with Q-Learning (simple version)

## Aim
Train an agent with reinforcement learning to find its way through a maze.

## Problem Statement
An 8x8 grid maze with 23 wall cells, start at (0, 0) and goal at (7, 7). The agent moves up, right, down or left. Rewards: -1 per step, +20 for reaching the goal, -5 for hitting a wall.

## Steps followed
1. Define the maze grid and a step function with the rewards above.
2. Train a Q-table with Q-learning and an epsilon-greedy policy for 1500 episodes.
3. Walk the learned path greedily from start to goal.
4. Print the maze with the learned path drawn in.

## Output
- The agent reaches the goal; the printed maze shows the learned path (S = start, G = goal, # = wall, * = path).
