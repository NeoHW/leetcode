class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = set()
        max_fish = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue 
                
                cc_fish = self.bfs(i, j, n, m, visited, grid)
                max_fish = max(max_fish, cc_fish)

        return max_fish
    
    def bfs(self, i:int, j:int, n:int, m:int, visited:set, grid:List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        curr_fish = 0
        q = deque([(i,j)])
        visited.add((i,j))
        while q:
            x,y = q.popleft()
            curr_fish += grid[x][y]
            for dx,dy in dirs:
                newx, newy = x+dx, y+dy
                if newx in range(n) and newy in range(m) and (newx,newy) not in visited and grid[newx][newy] > 0:
                    q.append((newx,newy))
                    visited.add((newx,newy))
        
        return curr_fish