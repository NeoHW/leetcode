class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        dp = [float("inf")] * (n+1)
        dp[0] = 0 # 0 need 0 perfect squares

        # like coin change
        for i in range(1, n+1):
            for s in squares:
                if dp[i - s] + 1 < dp[i]:
                    dp[i] = dp[i - s] + 1
        
        return dp[n]