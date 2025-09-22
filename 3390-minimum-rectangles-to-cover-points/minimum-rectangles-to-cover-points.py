class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        if not points:
            return 0

        points.sort()
        res = 1
        curr_x = points[0][0] + w

        for x,_ in points:
            if x <= curr_x:
                continue
            
            res += 1
            curr_x = x + w
        
        return res
            