# Alpha-Beta Pruning Demo

def alpha_beta(depth, node_index, is_maximizing, values, alpha, beta, max_depth):
    # Base case: when we reach a leaf node
    if depth == max_depth:
        return values[node_index]
    
    if is_maximizing:
        best = float('-inf')
        # Two children per node (binary tree)
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            # Prune
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            # Prune
            if beta <= alpha:
                break
        return best


# Main code
if __name__ == "__main__":
    # Terminal nodes (leaf values)
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    print("Leaf Node Values:", values)

    # Depth of tree (3 levels → 8 leaves)
    max_depth = 3

    result = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), max_depth)
    
    print("\nThe optimal value for the maximizer is:", result)
