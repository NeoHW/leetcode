class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int ans = 0;
        
        for (int i = 0; i <= n-3; i++) {
            for (int j = 0; j <= m-3; j++) {
                if (isMagicSquare(grid, i, j)) {
                    ans++;
                }
            }
        }
        return ans;
    }

private:
    bool isMagicSquare(vector<vector<int>>& grid, int y, int x) {
        vector<int> count(10, 0);
        for (int i = y; i < y+3; i++) {
            for (int j = x; j < x+3; j++) {
                int num = grid[i][j];
                if (num < 1 || num > 9 || ++count[num] > 1) {
                    return false;
                }
            }
        }

        int rowSum1 = grid[y][x] + grid[y][x+1] + grid[y][x+2];
        int rowSum2 = grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2];
        int rowSum3 = grid[y+2][x] + grid[y+2][x+1] + grid[y+2][x+2];

        int colSum1 = grid[y][x] + grid[y + 1][x] + grid[y + 2][x];
        int colSum2 = grid[y][x + 1] + grid[y + 1][x + 1] + grid[y + 2][x + 1];
        int colSum3 = grid[y][x + 2] + grid[y + 1][x + 2] + grid[y + 2][x + 2];

        int diagonalSum1 = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2];
        int diagonalSum2 = grid[y][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x];

        if (rowSum1 == 15 && rowSum2 == 15 && rowSum3 == 15 &&
            colSum1 == 15 && colSum2 == 15 && colSum3 == 15 &&
            diagonalSum1 == 15 && diagonalSum2 == 15) {
            return true;
        }
        return false;
    }
};