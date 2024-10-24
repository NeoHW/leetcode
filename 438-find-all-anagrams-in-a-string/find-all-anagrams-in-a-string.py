class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window of length p
        result = []
        p_count = Counter(p)
        s_count = Counter()
        p_len = len(p)

        for i in range(len(s)):
            # Add the current character to the window's count
            s_count[s[i]] += 1
            
            # When the window's size exceeds the length of p, remove the leftmost character
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1

            # If the frequency counts match, we found an anagram
            if s_count == p_count:
                result.append(i - p_len + 1)
        
        return result