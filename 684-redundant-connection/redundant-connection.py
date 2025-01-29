class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parents = {i:-1 for i in range(1,n+1)} 

    def find(self, node):
        if self.parents[node] == -1:
            return node
        
        root = self.find(self.parents[node])
        self.parents[node] = root
        return root
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        self.parents[p2] = p1
        self.count -= 1
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)) 
        for v,w in edges:
            if not uf.union(v,w):
                return [v,w]
        
        return []