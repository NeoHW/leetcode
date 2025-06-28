class Solution {
public:
    typedef pair<int,int> P;
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        priority_queue<P, vector<P>, std::greater<P>> pq;

        for (int i = 0; i < nums.size(); ++i) {
            pq.push({nums[i], i});
            if (pq.size() > k) {
                pq.pop();
            }
        }

        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        // sort by index to preserver order
        sort(res.begin(), res.end());

        for (int i = 0; i < res.size(); ++i) {
            res[i] = nums[res[i]];
        }

        return res;
    }
};