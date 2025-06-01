from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True  # If the source and destination are the same, return True
        
        graph = defaultdict(list)

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS Initialization
        queue = deque([source])
        visited = set([source])

        # BFS Traversal
        while queue:
            node = queue.popleft()
            if node == destination:
                return True  # Found a path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False  # No path found
