class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        # iterate twice 
        for i in range(2*n):
            j = i % n
            while stack and nums[j] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[j]
            # push only real indices during first appearance
            if i < n:
                stack.append(j)
        
        return res