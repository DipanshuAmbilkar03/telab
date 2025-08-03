from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited_dfs = set()

def dfs(node):
    if node not in visited_dfs:
        print(node, end=' ')
        visited_dfs.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

print("DFS:")
dfs('A')
print("\nBFS:")
bfs('A')
