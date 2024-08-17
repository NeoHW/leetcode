class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        // furthest track furthest index we can reach from current index
        // end indicates end of current jump range
        int jumps = 0, furthest = 0, end = 0;

        for (int i = 0; i < n - 1; i++) {
            furthest = max(furthest, i + nums[i]);
            if (i == end) {
                jumps++;
                end = furthest;
            }
        }

        return jumps;
    }
};