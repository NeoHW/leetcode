class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort using khan's algo
        AL = defaultdict(list)
        in_degree = defaultdict(int)
        visited = set()
        res = []

        # set up AL & indegree
        for curr, prereq in prerequisites:
            AL[prereq].append(curr)
            in_degree[curr] += 1
        
        # adding in nodes with in_degree of 0
        q = deque()
        for i in range(numCourses): # cannot iterate through defaultdict as the keys with 0 count wont be present
            if in_degree[i] == 0:
                q.append(i)
        
        
        # topological sort
        while q:
            node = q.pop()
            res.append(node)

            for neighbour in AL[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0 and neighbour not in visited:
                    q.append(neighbour)
        
        return res if len(res) == numCourses else []