class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // cost[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        int n = cost.size();

        int prev = 0, curr = 0;
        vector<int> dp(n+1, 0); // as it is only counted if we reach outside the array

        for (int i = 2; i <= n; i++) {
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1]);
        }

        return dp[n];
    }
};