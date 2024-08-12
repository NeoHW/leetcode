class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        // dp[i][j] = max score diff for either player if game played from i to j
        // dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])

        int n = piles.size();
        vector<vector<int>> dp(n, vector<int>(n,0));
        
        // if only one pile to choose from, difference will be that pile's stones
        for (int i = 0; i < n; i++) {
            dp[i][i] = piles[i];
        }

        for (int d = 1; d < n; d++) { // size of subarray (start from size 2 to n), solve smaller subproblem
            for (int i = 0; i < n - d; i++) { // start & end index of subarray
                dp[i][i+d] = max(piles[i] - dp[i+1][i+d], piles[i+d] - dp[i][i+d-1]);
            }
        }
        
        return dp[0][n-1] > 0;
    }
};