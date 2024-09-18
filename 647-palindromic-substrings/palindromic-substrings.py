class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1 # one letter is a palindrome
            count += 1
            for j in range(i):
                if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    count += 1
        
        return count
