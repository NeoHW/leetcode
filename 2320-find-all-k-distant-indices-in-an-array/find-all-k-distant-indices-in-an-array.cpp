class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n = nums.size();
        unordered_set<int> hs;

        for (int i = 0; i < n; ++i) {
            if (nums[i] != key) continue;
            
            for (int j = i - k; j <= i + k; ++j) {
                if (j >= 0 && j < n) {
                    hs.insert(j);  // Mark as k-distant
                }
            }
        }

        vector<int> res(hs.begin(), hs.end());
        sort(res.begin(), res.end());

        return res;
    }
};