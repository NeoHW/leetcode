class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane algo, find the largest subarray sum
        curr_diff, max_so_far = 0,0

        for i in range(1, len(prices)):
            curr_diff += prices[i] - prices[i-1]
            if curr_diff < 0: # found prices[i] lower than time we ought, buy here instead
                curr_diff = 0
            max_so_far = max(max_so_far, curr_diff)
        
        return max_so_far