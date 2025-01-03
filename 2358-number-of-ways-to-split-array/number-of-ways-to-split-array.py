class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)

        valid_pairs = 0
        for i in range(n-1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                valid_pairs += 1
        
        return valid_pairs