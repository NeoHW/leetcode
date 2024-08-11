class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        // UFDS method
        // track number of cycles formed, new cycle = new region

        int gridSize = grid.size();
        int pointsPerSide = gridSize + 1;
        int totalPoints = pointsPerSide * pointsPerSide;

        vector<int> parentArray(totalPoints, -1);

        for (int i = 0; i < pointsPerSide; i++) {
            for (int j = 0; j < pointsPerSide; j++) {
                // border will be 0 (same parent for inital big section)
                if (i == 0 || j == 0 || i == pointsPerSide - 1 || j == pointsPerSide - 1) {
                    parentArray[i * pointsPerSide + j] = 0; 
                }
            }
        }

        // set parent at top-left corner to itself
        parentArray[0] = -1;
        int regionCount = 1;

        // Process each cell in the grid
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                if (grid[i][j] == '/') {
                    int topRight = i * pointsPerSide + (j + 1);
                    int bottomLeft = (i + 1) * pointsPerSide + j;
                    regionCount += union_sets(parentArray, topRight, bottomLeft);
                } else if (grid[i][j] == '\\') {
                    int topLeft = i * pointsPerSide + j;
                    int bottomRight = (i + 1) * pointsPerSide + (j+1);
                    regionCount += union_sets(parentArray, topLeft, bottomRight);
                }
            }
        }
        return regionCount;
    }

private:
    //UFDS: find parent of a set
    int find(vector<int>& parentArray, int node) {
        if (parentArray[node] == -1) {
            return node;
        }

        return parentArray[node] = find(parentArray, parentArray[node]);
    }

    // Union two sets and return 1 if a new region is formed, 0 otherwise
    int union_sets(vector<int>& parentArray, int node1, int node2) {
        int parent1 = find(parentArray, node1);
        int parent2 = find(parentArray, node2);

        if (parent1 == parent2) {
            return 1; // Nodes are already in same set, new region formed
        }

        parentArray[parent2] = parent1; // union the sets
        return 0; // no new region formed
    }
};