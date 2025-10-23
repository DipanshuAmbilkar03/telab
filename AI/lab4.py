# Alpha-Beta Pruning Example (Game Tree Search)
import math
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
maxDepth = 3

print("Game Tree Leaf Node Values:", values)
optimal_value = alpha_beta(0, 0, True, values, -math.inf, math.inf, maxDepth)

print("\nThe Optimal Value is:", optimal_value)
