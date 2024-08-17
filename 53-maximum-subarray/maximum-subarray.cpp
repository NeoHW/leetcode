class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // kadane algorithm
        int maxSoFar = INT_MIN;
        int currMax = 0;

        for (int c : nums) {
            // we only need to compare (currMax + next) vs next single element 
            currMax = max(currMax + c, c);
            maxSoFar = max(maxSoFar, currMax);
        }

        return maxSoFar;
        
        
        /*
        int maxSoFar = INT_MIN;
        int maxEndingHere = 0;

        for (int i = 0; i < nums.size(); i++) {
            maxEndingHere += nums[i];
            maxSoFar = max(maxSoFar, maxEndingHere);

            // if maxEndingHere at curr index goes negative, start from 0
            maxEndingHere = max(maxEndingHere, 0);
        }

        return maxSoFar;
        */
    }
};