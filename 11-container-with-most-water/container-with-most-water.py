class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) - 1

        # we only move the shorter side (the limiting side)
        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return res