class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        res = 0
        curr_x = -1

        for x,_ in points:
            if x > curr_x:
                res += 1
                curr_x = x + w
        
        return res