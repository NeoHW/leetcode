class Solution {
public:
    int rotatedDigits(int n) {
        // 3,4,7 are invalid (dp[i] = 0)
        // 0,1,8 rotates to themselves (dp[i] = 1)
        // 2,5,6,9 valid, will change to diff number (dp[i] = 2)

        // idea for DP: build up sub-solutions in multiples of 10

        vector<int> dp(n+1, 0);
        int ans = 0;

        for (int i = 0; i <= n; i++) {
            // build out first 10 digits (0-9) manually
            if (i < 10) {
                if (i == 0 || i == 1 || i == 8) {
                    dp[i] = 1;
                } else if (i == 2 || i == 5 || i == 6 || i == 9) {
                    dp[i] = 2;
                    ans++;
                }
            } else {
                // e.g. split 32 -> 3 and 2
                // e.g. split 322 -> 32 and 2
                int firstPart = dp[i / 10];
                int secondPart = dp[i % 10];
                if (firstPart == 1 && secondPart == 1) {
                    dp[i] = 1;
                } else if (firstPart >= 1 && secondPart >= 1) {
                    dp[i] = 2;
                    ans++;
                }
            }
        }
        return ans;
    }
};