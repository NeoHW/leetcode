class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> hs;
        int l = 0, r = 0, n = nums.size();
        int curr = 0, res = 0;

        while (r < n) {
            while (hs.contains(nums[r])) {
               hs.erase(nums[l]);
               curr -= nums[l];
               ++l;
            }

            hs.insert(nums[r]);
            curr += nums[r];
            res = std::max(res, curr);
            ++r;
        }

        return res;
    }
};