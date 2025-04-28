class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(0, n-2):
            if (nums[i] + nums[i+2]) * 2 == (nums[i+1]):
                res += 1
        return res