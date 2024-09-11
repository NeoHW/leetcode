class Solution:
    def rob(self, nums: List[int]) -> int:
        # house robber 1 for (0, n-1) and (1, n)
        n = len(nums)
        
        if n == 1:
            return nums[0]

        def houserobber(start, end) -> int:
            prev, curr = 0,0
            
            for i in range(start, end):
                temp = max(nums[i] + prev, curr)
                prev = curr
                curr = temp
            return curr
        
        return max(houserobber(0, n-1), houserobber(1, n))