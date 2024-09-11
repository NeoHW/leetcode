class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        maxArea = 0 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # do bfs here
                    count = 0
                    q = deque()
                    q.append((i,j))
                    visited.add((i,j))

                    while q:
                        x,y = q.pop()
                        count += 1
                        for dx,dy in directions:
                            newx, newy = x + dx, y + dy
                            if newx in range(m) and newy in range(n) and grid[newx][newy] == 1 and (newx, newy) not in visited:
                                q.append((newx, newy))
                                visited.add((newx, newy))

                    maxArea = max(maxArea, count)
        
        return maxArea