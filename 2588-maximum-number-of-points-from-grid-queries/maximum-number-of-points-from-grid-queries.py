class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # since queries are given to us beforehand, we can sort it and build up our answer instead!
        m, n = len(grid), len(grid[0])
        k = len(queries)
        res = [0] * k
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        pq = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        
        points = 0

        for val,idx in sorted_queries:
            while pq and pq[0][0] < val:
                cell_val, x, y = heapq.heappop(pq)
                points += 1
                for dx, dy in directions:
                    newx, newy = x + dx, y + dy
                    if newx in range(m) and newy in range(n) and (newx,newy) not in visited:
                        heapq.heappush(pq, (grid[newx][newy], newx, newy))
                        visited.add((newx, newy))
            
            res[idx] = points
        
        return res