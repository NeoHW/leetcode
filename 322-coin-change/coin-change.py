class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp from 1 to amount
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 # base case: 0 coins to make $0

        # imagine coins = [1,2,5], amount = 11
        # using $1, need dp[10] + 1
        # using $2, need dp[9] + 1
        # using $5, need dp[6] + 1

        for i in range(1, amount+1):
            for coin in coins: # loop through the coins to find out which one is lowest from dp
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1