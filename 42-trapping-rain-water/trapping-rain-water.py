class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0

        while l < r:
            if max_left <= max_right:
                l += 1
                # limited by maxl height
                # find how much water can be filled at this index
                res += max(0, max_left - height[l]) # max with 0 as we dont want it to be negative
                max_left = max(max_left, height[l])

            else:
                r -= 1
                # limited by max_right height
                # find how much water can be filled at this index
                res += max(0, max_right - height[r]) # max with 0 as we dont want it to be negative
                max_right = max(max_right, height[r])
        
        return res