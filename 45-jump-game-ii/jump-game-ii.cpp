class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        int l = 0, r = 0;

        while (r < n - 1) {
            int furthest = 0;
            // find the furthest we can go in the window from l to r
            for (int i = l; i <= r; i++) {
                furthest = max(furthest, i + nums[i]);
            }
            // move the window range
            l = r+1;
            r = furthest;
            ans++;
        }

        return ans;
    }
};