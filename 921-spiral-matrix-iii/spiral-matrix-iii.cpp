class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int n = rows * cols;
        int visited = 0;
        int stepsToMove = 1; // cycle is : 1,1,2,2,3,3,4,4...

        vector<vector<int>> directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int dirIndex = 0;

        vector<vector<int>> ans;
        ans.push_back({rStart, cStart});
        visited++;
        
        // cout << "Starting at: (" << rStart << ", " << cStart << ")" << endl;

        while (visited < n) {
            for (int i = 0; i < 2; i++) {
                auto direction = directions[dirIndex % 4];
                // cout << "Direction: (" << direction[0] << ", " << direction[1] << ")" << endl;
                for (int step = 0; step < stepsToMove; step++) {
                    rStart += direction[0];
                    cStart += direction[1];
                    // cout << "Moved to: (" << rStart << ", " << cStart << ")" << endl;
                    if ((rStart >= 0 && rStart < rows) && (cStart >= 0 && cStart < cols)) {
                        ans.push_back({rStart, cStart});
                        visited++;
                        // cout << "Visited: " << visited << " - (" << rStart << ", " << cStart << ")" << endl;
                        if (visited == n) {
                            return ans;
                        }
                    }
                }
                dirIndex++;
            }
            stepsToMove++;
            // cout << "Steps to move increased to: " << stepsToMove << endl;
        }
        return ans;
    }
};