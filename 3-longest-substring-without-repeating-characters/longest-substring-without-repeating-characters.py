class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l,r = 0,0
        ans = 0

        while r < len(s):
            if s[r] not in hs:
                hs.add(s[r])
                substring_length = r - l + 1
                ans = max(ans, substring_length)
                r += 1
                continue

            while (s[r] in hs) and (l < r):
                hs.remove(s[l])
                l += 1

        return ans