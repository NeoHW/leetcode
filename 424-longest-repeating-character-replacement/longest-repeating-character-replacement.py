class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int) # map char to their counts, max 26 alphabet, O(1)
        ans = 0
        l = 0

        # increase r, if fail condition, then slide the whole window forward
        # because we want the longest window, can just keep the length of longest window found
        for r in range(len(s)):
            hm[s[r]] += 1
            length_substring = r - l + 1
            max_count = max(hm.values())
            
            # want to get (length of substring - maxCount) to check if <= k    
            if (length_substring - max_count) <= k:
                ans = max(ans, length_substring)
            else:
                hm[s[l]] -= 1
                l += 1
        return ans