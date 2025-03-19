class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i,num in enumerate(nums):
            if num == 0 and i <= n - 3:
                res += 1
                for j in range(i, i+3):
                    nums[j] = nums[j] ^ 1  # bit manipulation
        
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1

        return res 