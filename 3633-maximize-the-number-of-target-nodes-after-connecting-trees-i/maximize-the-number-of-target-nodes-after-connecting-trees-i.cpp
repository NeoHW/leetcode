class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n = edges1.size() + 1, m = edges2.size() + 1;
        vector<vector<int>> AL1 = buildGraph(edges1);
        vector<vector<int>> AL2 = buildGraph(edges2);

        // best for tree 2 (distance ≤ k–1)
        int best2 = 0;
        if (k > 0) {
            for (int v = 0; v < m; ++v) {
                best2 = max(best2, bfs(AL2, v, k-1));
            }
        }

        // for each node in tree 1, count nodes ≤ k in tree 1 + best2
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = bfs(AL1, i, k) + best2;
        }

        return ans;
    }

private:
    vector<vector<int>> buildGraph(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> AL(n);
        
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            AL[u].push_back(v);
            AL[v].push_back(u);
        }

        return AL;
    }

    int bfs(vector<vector<int>> AL, int root, int max_depth) {
        int res = 1;
        queue<int> q;
        vector<bool> visited(AL.size(), false);

        q.push(root);
        visited[root] = true;

        while (max_depth-- > 0) {
            int curr_size = q.size();
            while (curr_size-- > 0) {
                int node = q.front();
                q.pop();

                for (int neighbour : AL[node]) {
                    if (visited[neighbour]) continue;

                    q.push(neighbour);
                    visited[neighbour] = true;
                    res++;
                }
            }
        }

        return res;
    }
};