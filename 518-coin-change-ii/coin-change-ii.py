class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # recurrence relation: dp[curr_amount] += dp[curr_amount - coin]
        
        # dp array of up to amount 
        dp = [0] * (amount + 1)
        dp[0] = 1 # 1 way to make up $0

        # process coins first to ensure unique combination
        for coin in coins:
            for curr_amount in range(coin, amount + 1):
                dp[curr_amount] += dp[curr_amount - coin] 
        
        return dp[amount]