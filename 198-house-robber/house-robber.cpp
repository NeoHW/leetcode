class Solution {
public:
    int rob(vector<int>& nums) {
        // recursive relation: 
        // rob(i) = max(rob(i-2) + currentHouseValue, rob(i-1))

        if (nums.size() == 0) {
            return 0;
        }

        int prev1 = 0;
        int prev2 = 0;
        // [prev2, prev1, n , n+1, ...]

        for (int num : nums) {
            int temp = max(prev2 + num, prev1);
            prev2 = prev1;
            prev1 = temp;
        }
        return prev1;
    }
};