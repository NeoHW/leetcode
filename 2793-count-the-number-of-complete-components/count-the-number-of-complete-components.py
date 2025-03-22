class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # UFDS
        # For each component: CCC if number of edges == k × (k - 1) / 2
        # where k = number of nodes

        uf = UnionFind(n)

        for v,w in edges:
            uf.union(v,w)
        
        return uf.countCompletedConnectedComponents()

class UnionFind:
    def __init__(self, n: int):
        self.count = n
        self.parents = {i:-1 for i in range(n)}
        self.size = {i:1 for i in range(n)} # number of nodes
        self.edge_count = {i:0 for i in range(n)} # number of edges
    
    def find(self, num):
        if self.parents[num] == -1:
            return num
        
        root = self.find(self.parents[num])
        self.parents[num] = root
        return root

    def union(self, num1, num2): 
        p1 = self.find(num1)
        p2 = self.find(num2)
    
        if p1 != p2:
            self.parents[p2] = p1
            self.size[p1] += self.size[p2]
            self.edge_count[p1] += self.edge_count[p2] + 1
            self.count -= 1
        else:
            self.edge_count[p1] += 1
    
    def countCompletedConnectedComponents(self):
        roots = set(self.find(i) for i in self.parents)
        count = 0
        for parent in roots:
            num_nodes = self.size[parent]
            num_edges = self.edge_count[parent]
            if num_edges == num_nodes * (num_nodes - 1) // 2:
                count += 1
        return count
