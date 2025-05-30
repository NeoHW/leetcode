class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();

        vector<int> AL(n, -1);
        for (int i = 0; i < n; ++i) {
            AL[i] = edges[i];
        }

        vector<int> dist1 = bfs(AL, node1);
        vector<int> dist2 = bfs(AL, node2);

        int res_node = -1;
        int min_dist = INT_MAX;

        for (int i = 0; i < n; ++i) {
            if (dist1[i] != -1 && dist2[i] != -1) {
                int curr_dist = max(dist1[i], dist2[i]);
                if (curr_dist < min_dist) {
                    min_dist = curr_dist;
                    res_node = i;
                }
            }
        }

        return res_node; 
    }

private:
    vector<int> bfs(vector<int>& AL, int root) {
        int n = AL.size();
        vector<bool> seen(n, false);
        vector<int> res(n, -1);

        // don't need queue as only max one outgoing edge
        int node = root;
        int dist = 0;

        while (node != -1 && !seen[node]) {
            seen[node] = true;
            res[node] = dist;
            node = AL[node];
            ++dist;
        }

        return res;
    }
};