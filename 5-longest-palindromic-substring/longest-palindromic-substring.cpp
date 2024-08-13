class Solution {
public:
    string longestPalindrome(string s) {
        // dp[i][j] tells us if substring from i to j is a palindrome
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int longest = 1;
        int startIndex = 0;
        int endIndex = 0;

        for (int i = 0; i < n; i++) {
            // every single character is a palindrome by itself
            dp[i][i] = true;

            for (int j = 0; j < i; j++) {
                if (s[j] == s[i] && (i-j <= 2 || dp[j+1][i-1])) {
                    dp[j][i] = true;
                    if (i - j + 1 > longest) {
                        longest = i - j + 1;
                        startIndex = j;
                        endIndex = i;
                    }
                }
            }
        }

        return s.substr(startIndex, endIndex-startIndex+1);
    }
};