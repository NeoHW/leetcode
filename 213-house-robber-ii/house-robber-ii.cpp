class Solution {
public:
    int rob(vector<int>& nums) {
        // use "house robber 1" to run from subarray[0,n-2] and subarray[1,n-1]
        int n = nums.size();
        return max({nums[0], robsub(nums, 0, n-2), robsub(nums, 1, n-1)});
    }

private:
    int robsub(vector<int>& nums, int start, int end) {
        int rob2 = 0, rob1 = 0;

        // [rob2, rob1, n, ...]
        for (int i = start; i <= end; i++) {
            int currNum = nums[i];
            int temp = max(currNum + rob2, rob1);
            rob2 = rob1;
            rob1 = temp;
        }
        // cout << "robsub(" << start << ", "<< end << ") \n";
        // cout << rob1 << endl;
        return rob1;
    }
};