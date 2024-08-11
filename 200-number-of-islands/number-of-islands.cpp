class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size(); 
        int m = grid[0].size();
        int ans = 0;

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r][c] == '1') {
                    bfs(grid, r, c, n, m);
                    ans++;
                }
            }
        }
        return ans;
    }

private:
    void bfs(vector<vector<char>>& grid, int r, int c,  int n, int m) {
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        queue<pair<int,int>> q;

        q.push({r,c});
        grid[r][c] = '0';

        while (!q.empty()) {
            auto [row,col] = q.front();
            q.pop();

            for (auto [x,y] : directions) {
                int nr = x + row;
                int nc = y + col;

                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1') {
                    q.push({nr,nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }
};