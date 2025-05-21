class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // for O(1) space, use first cell of every row and col as a flag.
        // but matrix[0][0]) is shared by both the first row and first column
        // var col0 to track if the first column needs to be zeroed.
        int col0 = 1;
        int rows = matrix.size(), cols = matrix[0].size();
        
        for (int i = 0; i < rows; ++i) {
            if (matrix[i][0] == 0) col0 = 0;
            for (int j = 1; j < cols; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            } 
        }
        
        // go bottom up to avoid overwriting marker values early
        for (int i = rows-1; i >= 0; --i) {
            for (int j = cols-1; j >= 1; --j) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
            // take note to rmb to do for col0
            if (col0 == 0) matrix[i][0] = 0;
        }
    }
};