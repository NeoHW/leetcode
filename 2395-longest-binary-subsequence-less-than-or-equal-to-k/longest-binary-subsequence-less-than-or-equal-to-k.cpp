class Solution {
public:
    int longestSubsequence(string s, int k) {
        // greedy longest contiguous suffix , and all 0s to the left of it
        int sum = 0, count = 0;
        int valid_bit_length = 32 - __builtin_clz(k);

        for (int i = 0; i < s.size(); ++i) {
            char ch = s[s.size() - 1 - i];
            if (ch == '1') {
                if (i < valid_bit_length && sum + (1 << i) <= k) {
                    sum += 1 << i;
                    ++count;
                }
            } else {
                ++count;
            }
        }

        return count;
    }
};