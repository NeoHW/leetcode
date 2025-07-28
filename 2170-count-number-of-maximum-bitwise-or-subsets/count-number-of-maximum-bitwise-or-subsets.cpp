class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        // OR is a non decreasing monotonic operator
        int max_value = 0;
        for (const int num: nums) {
            max_value |= num;
        }
        return countSubsets(nums, 0, 0, max_value);
    }

private:
    int countSubsets(vector<int>& nums, int index, int current, int target) {
        if (index == nums.size()) {
            return (current == target) ? 1 : 0;
        }
        // either pick or dont pick the current index 
        int count_without = countSubsets(nums, index + 1, current, target);
        int count_with = countSubsets(nums, index + 1, current | nums[index], target);
        return count_without + count_with;
    }
};