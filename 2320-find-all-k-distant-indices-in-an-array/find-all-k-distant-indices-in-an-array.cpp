class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n = nums.size();
        vector<int> res;
        int smallest_index_not_added = 0;

        for (int i = 0; i < n; ++i) {
            if (nums[i] == key) {
                int l = max(smallest_index_not_added, i-k);
                smallest_index_not_added = min(n-1, i+k) + 1;
                for (int j = l; j < smallest_index_not_added; ++j) {
                    res.push_back(j);
                }
            } 
        }

        return res;
    }
};