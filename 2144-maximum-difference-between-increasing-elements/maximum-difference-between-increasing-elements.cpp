class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int n = nums.size();
        int res = -1, min_diff = nums[0];

        for (int i = 1; i < n; ++i) {
            if (nums[i] <= min_diff) {
                min_diff = nums[i];
            } else {
                res = max(res, nums[i] - min_diff);
            }
        }

        return res;
    }
};