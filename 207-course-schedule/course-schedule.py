class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topo sort using kahn's

        AL = defaultdict(list) # store prereq -> course
        inDegree = defaultdict(int) # store count
        
        for course, prereq in prerequisites:
            AL[prereq].append(course)
            inDegree[course] += 1
        
        q = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        visited = 0
        while q:
            curr = q.popleft()
            visited += 1
            for neighbour in AL[curr]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    q.append(neighbour)
        
        return visited == numCourses