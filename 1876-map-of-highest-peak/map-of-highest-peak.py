class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        n,m = len(isWater), len(isWater[0])
        visited = set()
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i,j,0))
                    visited.add((i,j))
                isWater[i][j] = 0
        
        while q:
            x,y,v = q.popleft()
            newv = v + 1
            for dx,dy in directions:
                newx, newy = x+dx, y+dy
                if newx in range(n) and newy in range(m) and (newx, newy) not in visited:
                    isWater[newx][newy] = newv
                    visited.add((newx, newy))
                    q.append((newx, newy, newv))
        
        return isWater