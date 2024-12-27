class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[index][sum] = number of ways to reach sum using first index numbers
        
        total_sum = sum(nums)
        # our dp table is [nums.length][2 * totalSum + 1] to represent both +ve & -ve sums
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # note our DP table is something like [-3,-2,-1,0,1,2,3]
        # base case for first row(index)
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] += 1

        for index in range(1, len(nums)):
            for sum_val in range(-total_sum, total_sum + 1):
                # if this current sum is achievable from previous numbers
                if dp[index-1][sum_val + total_sum] > 0:
                    dp[index][sum_val + nums[index] + total_sum] += dp[index - 1][sum_val + total_sum]
                    dp[index][sum_val - nums[index] + total_sum] += dp[index - 1][sum_val + total_sum]
        
        return 0 if abs(target) > total_sum else dp[len(nums) - 1][target + total_sum]