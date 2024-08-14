class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0, n = s.size();
        int longest = 0;

        unordered_set<char> hs;

        while (r < n) {
            if (!hs.contains(s[r])) {
                hs.insert(s[r]);
                r++;
                longest = max(longest, r - l);
            }

            while (hs.contains(s[r]) && l < r) {
                hs.erase(s[l]);
                l++;
            }
        }

        return longest;
    }
};