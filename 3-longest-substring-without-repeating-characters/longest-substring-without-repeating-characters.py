class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(s)):
            hm[s[r]] += 1
            have_duplicate = False

            for v in hm.values(): # 26 operations max, O(1)
                if v > 1:
                    have_duplicate = True
            
            if not have_duplicate:
                substring_length = r - l + 1
                ans = max(ans, substring_length)
            else:
                hm[s[l]] -= 1
                l += 1

        return ans