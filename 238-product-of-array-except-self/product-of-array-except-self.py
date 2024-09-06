class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]
        suffix = [1] * n
        res = [1] * n

        for i in range(1,n):
            prefix.append(prefix[-1] * nums[i-1])
        
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res