class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int res = 1;
        int start = nums[0];

        for (const auto& num: nums) {
            if (num - start > k) {
                start = num;
                ++res;
            }
        }

        return res;
    }
};