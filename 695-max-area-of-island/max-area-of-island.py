class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [n * [0] for _ in range(m)]
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    q = deque()
                    q.append((i,j))
                    visited[i][j] = 1
                    area = 1

                    while q:
                        x,y = q.popleft()
                        for dx,dy in directions:
                            newx, newy = x+dx, y+dy
                            if newx in range(m) and newy in range(n) and grid[newx][newy] == 1 and not visited[newx][newy]:
                                q.append((newx,newy))
                                visited[newx][newy] = 1
                                area += 1
                    
                    max_area = max(max_area,area)
        
        return max_area