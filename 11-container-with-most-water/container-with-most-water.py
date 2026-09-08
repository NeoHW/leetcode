class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        max_water = 0
        while l <= r:
            curr = (r-l) * min(height[l],height[r])
            max_water = max(max_water, curr)

            if height[l] <= height[r]:
                l += 1
                continue

            if height[r] < height[l]:
                r -= 1
                continue
        
        return max_water