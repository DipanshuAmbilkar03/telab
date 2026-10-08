# Practical 6: Taxi Problem with Q-Learning (simple version)

## Aim
Solve the taxi problem with reinforcement learning: the agent picks up a passenger at one location and drops them at their destination.

## Problem Statement (from the syllabus)
Solve the Taxi problem using reinforcement learning where the agent acts as a taxi driver to pick up a passenger at one location and then drop the passenger off at their destination.

## Steps followed
1. Build a simple 5x5 taxi grid: 4 corner locations (R, G, Y, B), 6 actions (move, pickup, dropoff).
2. Rewards: -1 per step, +20 for a correct drop-off, -10 for a wrong pick-up/drop-off.
3. Train a Q-table with Q-learning and an epsilon-greedy policy for 2000 episodes.
4. Run one greedy test episode and report the total reward.

## Output
- The learned agent picks up the passenger and reaches the destination, finishing with a positive total reward.
