class Solution {
public:
    int jump(vector<int>& nums) {
        // recursive relation: minJumpsToEnd[i] = 1 + min(minJumpsToEnd[i+1], minJumpsToEnd[i+2] ... minJumpsToEnd[i+k]) : where k = nums[i]
        int n = nums.size();
        vector<int> dp(n, INT_MAX);
        
        // base case: no need to jump when you're already there
        dp[n-1] = 0;

        for (int i = n-2; i >= 0; i--) {
            int minOfAllAfter = INT_MAX;
            for (int j = i+1; j <= i+nums[i] && j < n; j++) {
                minOfAllAfter = min(minOfAllAfter, dp[j]);
            }
            if (minOfAllAfter != INT_MAX) {
                dp[i] = 1 + minOfAllAfter;
            }
        }

        return dp[0];
    }
};