class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        max_area = 0

        while l < r:
            max_area = max(max_area, min(height[l],height[r]) * (r-l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
