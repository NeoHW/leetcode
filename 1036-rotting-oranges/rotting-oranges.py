class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        fresh = 0

        # find all rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        # simultaneous bfs
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in directions:
                    newx, newy = x+dx, y+dy
                    if newx in range(m) and newy in range(n) and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        q.append((newx,newy))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1