class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // intution: store a STRICTLY DECREASING deque
        // front of the deque would be the largest element in that window
        // then we will pop the front when left pointer goes past it

        deque<int> d;
        vector<int> ans;

        // populate the intial deque
        for (int i = 0; i < k; i++) {
            // don't have to keep any smaller elements than the max element in the initial window
            while (!d.empty() && nums[i] > d.back()) {
                d.pop_back();
            }
            d.push_back(nums[i]);
        }
        ans.push_back(d[0]);

        // slide the window
        int l = 0;
        for (int r = k; r < nums.size(); r++) {
            // remove front of deque if left pointer is that element
            if (nums[l] == d[0]) {
                d.pop_front();
            }
            l++;

            // add in right element
            while (!d.empty() && nums[r] > d.back()) {
                d.pop_back();
            }
            d.push_back(nums[r]);
            ans.push_back(d[0]);
        }

        return ans;
    }
};