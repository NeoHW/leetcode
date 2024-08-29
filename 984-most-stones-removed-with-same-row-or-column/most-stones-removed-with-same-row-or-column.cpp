class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        // find number of CCs using UDFS
        int n = stones.size();
        UnionFind uf(n);

        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    uf.unionNodes(i,j);
                }
            }
        }
        
        return n - uf.count;
    }

private:
    class UnionFind {
    public:
        int count; // count number of Connected components
        vector<int> parent; // array to keep track of each node's parent

        UnionFind(int n) {
            count = n;
            parent.resize(n, -1); // initialise all parent's to -1 (itself)
        }

        int findRoot(int node) {
            if (parent[node] == -1) {
                return node;
            }
            return parent[node] = findRoot(parent[node]); // directly assign root node to parent of each node
        }

        void unionNodes(int n1, int n2) {
            int root1 = findRoot(n1);
            int root2 = findRoot(n2);

            if (root1 == root2) {
                return; // already same component, do nothing
            }

            // merge components, reduce count of CCs
            count--;
            parent[root1] = root2;
        }
    };
};