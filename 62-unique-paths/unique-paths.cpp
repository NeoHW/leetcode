class Solution {
public:
    int uniquePaths(int m, int n) {
        // recursive relation: dp[i][j] = dp[i-1][j] + dp[i][j-1]

        // optimise space with 1d vector
        vector<int>dp(n,1);

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // get same column from prev row : dp[j] and
                // get prev column from same row: dp[j-1]
                dp[j] += dp[j-1];
            }
        }

        return dp[n-1];



        /*
        vector<vector<int>> dp(m, vector<int>(n,1)); // initalise all with 1 !

        // then we can start from i == 1 and j == 1
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                 dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }

        return dp[m-1][n-1];
        */
    }
};