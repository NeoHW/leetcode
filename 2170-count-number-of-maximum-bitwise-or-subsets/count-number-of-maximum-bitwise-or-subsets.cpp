class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        // OR is a non decreasing monotonic operator
        int max_value = 0;
        for (const int num: nums) {
            max_value |= num;
        }
        vector<vector<int>> memo (nums.size(), vector<int>(max_value + 1, -1)); // dp
        return countSubsets(nums, 0, 0, max_value, memo);
    }

private:
    int countSubsets(vector<int>& nums, int index, int current, int target, vector<vector<int>>& memo) {
        if (index == nums.size()) {
            return (current == target) ? 1 : 0;
        }

        if (memo[index][current] != -1) {
            return memo[index][current];
        }

        // either pick or dont pick the current index 
        int count_without = countSubsets(nums, index + 1, current, target, memo);
        int count_with = countSubsets(nums, index + 1, current | nums[index], target, memo);
        return memo[index][current] = count_without + count_with;
    }
};