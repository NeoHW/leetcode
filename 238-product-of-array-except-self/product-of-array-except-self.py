class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # do prefix sum first
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        
        # do backwards
        curr = 1
        for i in range(n-1,-1,-1):
            res[i] *= curr
            curr *= nums[i]
        
        return res