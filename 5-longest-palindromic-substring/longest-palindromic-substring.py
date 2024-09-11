class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = 0
        startIndex = 0
        endIndex = 0

        # dp[i][j] means substring from i to j is a palindrome
        dp = [n * [0] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1 # every letter itself is a palindrome
            for j in range(n):
                # same letter AND (only one letter in middle or middle is palindrome)
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    if (longest < i-j):
                        longest = i - j
                        startIndex = j
                        endIndex = i
        
        return s[startIndex:endIndex + 1]