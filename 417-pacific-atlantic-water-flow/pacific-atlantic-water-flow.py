class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 2 sets containing reachable points from atl and pac respectively
        m,n = len(heights), len(heights[0])
        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        pac, atl = set(), set()

        def dfs(i ,j, visited, prevHeight):
            if (i,j) in visited or i not in range(m) or j not in range(n) or heights[i][j] < prevHeight:
                return
            
            visited.add((i,j))

            for dx,dy in dir:
                dfs(i+dx, j+dy, visited, heights[i][j])
        
        for i in range(m):
            dfs(i, 0, pac, heights[i][0]) # pacific
            dfs(i, n-1, atl, heights[i][n-1]) # atlantic
        
        for i in range(n):
            dfs(0, i, pac, heights[0][i]) # pacific
            dfs(m-1, i, atl, heights[m-1][i]) # atlantic

        # find intersection using &
        return pac & atl
