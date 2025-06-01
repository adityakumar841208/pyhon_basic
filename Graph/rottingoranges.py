from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        entrance = deque()
        fresh = 0
        
        m , n = len(grid) , len(grid[0])
        
        for i in range(m):            
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    entrance.append([i,j,0])
                    
        if fresh == 0:
            return 0
        
               
        while entrance:
            x,y,steps = entrance.popleft()
            
            # perform rotting the oranges operation 
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx,ny = x+dx, y+dy
                
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    fresh = fresh - 1
                    if fresh == 0:
                        return steps + 1
                    grid[nx][ny] = 2
                    entrance.append([nx,ny,steps+1])
            
        return -1
        
solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4