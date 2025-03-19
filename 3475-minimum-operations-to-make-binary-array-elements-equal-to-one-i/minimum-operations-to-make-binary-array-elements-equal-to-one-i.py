class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i,num in enumerate(nums):
            if num == 0 and i <= n - 3:
                res += 1
                for j in range(i, i+3):
                    nums[j] = self.flip(nums[j])
        
        for i in range(n-3, n):
            if nums[i] == 0:
                return -1
        
        return res 


    def flip(self, num:int) -> int:
        if num == 0:
            return 1
        else:
            return 0