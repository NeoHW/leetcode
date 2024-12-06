class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int m = grid.size(), n = grid[0].size();

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, bfs(grid, m, n, i, j));
                }
            }
        }
        return maxArea;
    }

private:
    int bfs(vector<vector<int>>& grid, int m, int n,  int r, int c) {
        vector<vector<int>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        queue<pair<int,int>> q;

        q.push({r,c});
        grid[r][c] = 0;
        int area = 1;

        while (!q.empty()) {
            auto [row,col] = q.front();
            q.pop();

            for (const auto& dir : directions) {
                int x = dir[0];
                int y = dir[1];

                int nr = row + x;
                int nc = col + y;

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 0;
                    q.push({nr,nc});
                    ++area;
                }
            }
        }
        return area;
    }
};