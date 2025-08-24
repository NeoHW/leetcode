class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        curr = 0
        res = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            curr += nums[r]

            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                curr -= nums[l]
                l += 1
            
            res = max(res, r-l)
        
        return res