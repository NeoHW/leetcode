class Solution:
    def countGoodStrings(self, low: int, high: int, numZeros: int, numOnes: int) -> int:
        # Use dp[i] to record to number of good strings of length i.
        mod = 10 ** 9 + 7
        dp = [1] + [0] * high # empty string is good string of length 0

        for end in range(1, high + 1):
            if end >= numZeros:
                dp[end] += dp[end - numZeros]
            if end >= numOnes:
                dp[end] += dp[end - numOnes]
            dp[end] %= mod
        
        return sum(dp[low : high+1]) % mod