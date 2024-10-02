class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n = arr.size();
        priority_queue<pair<int,int>> pq; // max heap
        vector<int> ans(n);

        for (int i = 0; i < n; i++) {
            pq.push({-1 * arr[i], i}); // min heap
        }

        int prev = -1;
        int rank = 0;
        while (!pq.empty()) {
            auto p = pq.top();
            if (p.first != prev) {
                rank++;
            }
            ans[p.second] = rank;
            prev = p.first;
            pq.pop();
        }

        return ans;
    }
};