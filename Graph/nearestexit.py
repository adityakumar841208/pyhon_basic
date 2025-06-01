from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        q = deque([(*entrance, 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            x, y, steps = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if nx in {0, m - 1} or ny in {0, n - 1} and (nx, ny) != entrance:
                        return steps + 1
                    maze[nx][ny] = '+'
                    q.append((nx, ny, steps + 1))
                        
        return -1

# dummy data
# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1        