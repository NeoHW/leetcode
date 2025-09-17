class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def LCS(i,j):
            if i < 0 or j < 0: return 0 # 0-based indexing string
            return 1+LCS(i-1,j-1) if text1[i] == text2[j] else max(LCS(i, j-1), LCS(i-1, j))
        
        return LCS(len(text1)-1, len(text2)-1)