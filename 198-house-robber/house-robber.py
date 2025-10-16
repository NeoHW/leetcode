class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob every alt house starting from i = 0 or i = 1
        n = len(nums)

        if n == 1:
            return nums[0]
        
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            temp = curr
            curr = max(curr, prev + nums[i])
            prev = temp
        
        return curr