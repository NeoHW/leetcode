class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        // use difference arrays 
        int n = nums.size();
        vector<int> diff(n + 1, 0);

        for (const auto &query : queries) {
            auto left = query[0];
            auto right = query[1];

            diff[left] += -1;
            diff[right + 1] -= -1;;
        }

        // update with prefix sum, and update nums at the same time
        int curr = 0;
        for (int i = 0; i < n; ++i) {
            curr += diff[i];
            nums[i] += curr;
        }

        for (int num : nums) {
            if (num > 0) return false;
        }

        return true;
    }
};