class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // kadane algorithm
        int maxSoFar = INT_MIN;
        int maxEndingHere = 0;

        for (int i = 0; i < nums.size(); i++) {
            maxEndingHere += nums[i];
            maxSoFar = max(maxSoFar, maxEndingHere);

            // if maxEndingHere at curr index goes negative, start from 0
            maxEndingHere = max(maxEndingHere, 0);
        }

        return maxSoFar;
    }
};