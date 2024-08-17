class Solution {
public:
    bool canJump(vector<int>& nums) {
        // car & gas method 
        int gas = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            // take one unit of gas to reach the next index
            gas--;

            if (gas < 0) {
                return false;
            }

            // at each "stop", either we refill or we keep on going
            gas = max(gas, nums[i]);
        }
        
        return true;
    }
};