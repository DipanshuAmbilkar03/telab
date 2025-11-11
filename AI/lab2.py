import heapq

# Node class for each position in the grid
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

# Manhattan distance heuristic function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search function
def a_star_search(grid, start, goal):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Goal check
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get start → goal

        # Possible moves (Right, Down, Left, Up)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in neighbors:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

            # Check valid move and avoid obstacles
            if (0 <= neighbor_pos[0] < len(grid) and 
                0 <= neighbor_pos[1] < len(grid[0]) and 
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0):

                if neighbor_pos in closed_list:
                    continue

                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_pos, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check if node already in open list with a better path
                if any(open_node.position == neighbor_node.position and open_node.f <= neighbor_node.f for open_node in open_list):
                    continue

                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example grid (0 = free, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Run A* search
path = a_star_search(grid, start, goal)

# Output
if path:
    print("Path found:", path)
else:
    print("No path found.")