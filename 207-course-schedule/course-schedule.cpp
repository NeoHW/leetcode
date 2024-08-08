class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        // topological sort
        vector<vector<int>> AL(n);
        vector<int> indegree(n,0);
        vector<int> ans;

        for (auto x : prerequisites) {
            AL[x[1]].push_back(x[0]);
            indegree[x[0]]++;
        }

        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            auto node = q.front();
            ans.push_back(node);
            q.pop();

            for (auto neighbour : AL[node]) {
                indegree[neighbour]--;
                if (indegree[neighbour] == 0) {
                    q.push(neighbour);
                }
            }
        }

        return ans.size() == n;
    }
};