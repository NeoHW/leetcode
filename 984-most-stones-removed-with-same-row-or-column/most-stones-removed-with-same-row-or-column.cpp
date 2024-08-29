class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        // for each cluster of stones, number of stones that can be removed is 
        // number of stones in that cluster - 1 (as we cant remove the last stone)
        // therefore, we can remove : total num stones - num of clusters

        int n = stones.size();
        vector<vector<int>> AL(n);

        // we store the index of stones instead of storing the stone pair
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                // Connect stones that share the same row or column
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    AL[i].push_back(j);
                    AL[j].push_back(i);
                }
            }
        }

        int clusters = 0;
        vector<bool> visited(n,false);

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(AL, visited, i);
                clusters++;
            }
        }

        return n - clusters;
    }

private:
    void dfs(vector<vector<int>>& AL, vector<bool>& visited, int currStone) {
        visited[currStone] = true;
        for (auto neighbour : AL[currStone]) {
            if (!visited[neighbour]) {
                dfs(AL, visited, neighbour);
            }
        }
    }
};