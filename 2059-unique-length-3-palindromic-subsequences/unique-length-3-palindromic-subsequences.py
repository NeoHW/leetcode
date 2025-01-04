class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        NUM_ALPHABETS = 26
        first = [-1] * NUM_ALPHABETS
        last = [-1] * NUM_ALPHABETS

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if first[index] == -1:
                first[index] = i
            last[index] = i
        
        res = 0

        for i in range(NUM_ALPHABETS):
            hs = set()
            for j in range(first[i] + 1, last[i]):
                hs.add(s[j])
            res += len(hs)
        
        return res