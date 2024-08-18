class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        int l = 0, r = 0;
        int ones = 0, zeros = 0;
        int ans = 0;

        while (r < s.size()) {
            if (s[r] == '0') {
                zeros++;
            } else {
                ones++;
            }

            // shrink window till meet requirements if overshot
            while (zeros > k && ones > k) {
                if (s[l] == '0') {
                    zeros--;
                } else {
                    ones--;
                }
                l++;
            }

            // all substrings starting from l to r are valid
            ans += (r - l + 1);
            r++;
        }

        return ans;
    }
};