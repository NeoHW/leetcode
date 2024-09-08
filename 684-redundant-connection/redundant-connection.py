class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = {i:-1 for i in range(1, n+1)} # 1 based indexing in question!
    
    def find(self, node):
        if self.parent[node] == -1:
            return node
        
        root = self.find(self.parent[node])
        self.parent[node] = root
        return root

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        
        if p1 != p2:
            self.parent[p2] = p1
            self.count -= 1
            return True
        
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for v,w in edges:
            if not uf.union(v,w):
                return [v,w]
        
        return []