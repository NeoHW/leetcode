class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        // dp question
        // dp[j] is max points for each cell in current row
        int n = points.size();
        int m = points[0].size();
        vector<long long> dp(m);

        // initialise dp with first row
        for (int j = 0; j < m; j++) {
            dp[j] = points[0][j];
        }

        // from second row onwards
        for (int i = 1; i < n; i++) {
            // represents the highest number you can add into from previous row
            vector<long long> left(m);
            vector<long long> right(m);

            // precompute left to right max
            left[0] = dp[0];
            for (int j = 1; j < m; j++) {
                // max(max point value from left and shift by one(penalty), take point above w/o penalty)
                left[j] = max(left[j-1] - 1, dp[j]);
            }

            // precompute right to left max
            right[m-1] = dp[m-1];
            for (int j = m-2; j >= 0; j--) {
                right[j] = max(right[j+1] - 1, dp[j]);
            }

            // compute new dp values for current row
            for (int j = 0; j < m; j++) {
                dp[j] = points[i][j] + max(left[j], right[j]);
            }
        }

        return *max_element(dp.begin(), dp.end());
    }


};