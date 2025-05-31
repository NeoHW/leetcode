class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        bool go_right = true;

        // generate flattened 1d array
        vector<int> flattened_arr;
        flattened_arr.push_back(0); // dummy value to make 1-index
        for (int i = n-1; i >= 0; --i){
            if (go_right) {
                for (int j = 0; j < n; ++j) {
                    flattened_arr.push_back(board[i][j]);
                }
            } else {
                for (int j = n-1; j >= 0; --j) {
                    flattened_arr.push_back(board[i][j]);
                }
            }
            go_right = !go_right;
        }

        // now can 1d bfs
        vector<bool> visited(n*n+1,false);
        queue<int> q;
        q.push(1);
        visited[1] = true;
        int steps = 0;

        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                int curr = q.front();
                q.pop();
                if (curr == n*n) return steps;

                for (int j = 1; j <= 6; ++j) {
                    int next = curr + j;
                    if (next > n * n) continue;
                    if (flattened_arr[next] != -1) {
                        next = flattened_arr[next];
                    }

                    if (!visited[next]) {
                        visited[next] = true;
                        q.push(next);
                    }
                }
            }
            ++steps;
        }

        return -1;
    }
};