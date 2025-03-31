class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if self.canStealWithCapability(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def canStealWithCapability(self, nums, k, capability):
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2
            else:
                i += 1
        return count >= k