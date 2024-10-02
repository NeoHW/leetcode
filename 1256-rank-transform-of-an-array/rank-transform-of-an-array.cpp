class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n = arr.size();
        priority_queue<pair<int,int>> pq; // max heap
        vector<int> ans(n);

        for (int i = 0; i < n; i++) {
            pq.push({-arr[i], i}); // min heap
        }

        int prev_value = INT_MIN;
        int rank = 0;

        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop();
            int value = -p.first;
            int index = p.second;

            if (value != prev_value) {
                rank++;
                prev_value = value;
            }

            ans[index] = rank;
        }

        return ans;
    }
};