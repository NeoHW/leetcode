class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # have 2 queues, one for pacific, one for atlantic, find common nodes
        m,n = len(heights), len(heights[0])
        dir = [(0,1), (1,0), (0,-1), (-1,0)]

        q1 = deque() # for pacific
        q2 = deque() # for atlantic
        visited_q1 = [n*[0] for i in range(m)]
        visited_q2 = [n*[0] for i in range(m)]

        for i in range(m):
            q1.append((i,0))
            q2.append((i,n-1))
            visited_q1[i][0] = 1
            visited_q2[i][n-1] = 1
        
        for i in range(n):
            q1.append((0,i))
            q2.append((m-1,i))
            visited_q1[0][i] = 1
            visited_q2[m-1][i] = 1

        def bfs(q, visited):
            while q:
                x,y = q.popleft()
                for dx,dy in dir:
                    newx, newy = dx+x, dy+y
                    if newx in range(m) and newy in range(n) and heights[x][y] <= heights[newx][newy] and not visited[newx][newy]:
                        q.append((newx,newy))
                        visited[newx][newy] = 1

        bfs(q1, visited_q1)
        bfs(q2, visited_q2)
        
        res = []
        for i in range(m):
            for j in range(n):
                if visited_q1[i][j] == 1 and visited_q2[i][j] == 1:
                    res.append([i,j])
        
        return res
