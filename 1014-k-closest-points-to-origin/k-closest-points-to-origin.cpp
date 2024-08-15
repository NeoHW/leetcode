class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // return k closest, means we only need to keep track of k elements
        priority_queue<pair<int,int>, vector<pair<int,int>>> maxHeap; // default compare by pair.first

        for (int i = 0; i < points.size(); i++) {
            // can compare without sqrt, use int instead of double
            int dist = points[i][0] * points[i][0] + points[i][1] * points[i][1];

            if (maxHeap.size() < k) {
                maxHeap.push({dist, i});
            } else if (dist < maxHeap.top().first) {
                maxHeap.pop();
                maxHeap.push({dist, i});
            }
        }

        // convert back to vector<vector<int>> from priority_queue<pair<int,int>
        vector<vector<int>> ans;
        while (!maxHeap.empty()) {
            ans.push_back(points[maxHeap.top().second]);
            maxHeap.pop();
        }

        return ans;
    }

};