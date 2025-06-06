class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)
        
        count = 0
        n = len(words)
    
        for i in range(n):
            for j in range(i):
                if isPrefixAndSuffix(words[j], words[i]):
                    count += 1
        
        return count