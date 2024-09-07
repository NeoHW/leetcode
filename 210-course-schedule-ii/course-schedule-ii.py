class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AL = {i : [] for i in range(numCourses)}
        inDegree = {i : 0 for i in range(numCourses)}

        q = deque()
        path = []

        for course, prereq in prerequisites:
            AL[prereq].append(course)
            inDegree[course] += 1
        
        for k,v in inDegree.items():
            if v == 0:
                q.append(k)

        count = 0
        while q:
            curr = q.popleft()
            path.append(curr)
            count += 1

            for neighbour in AL[curr]:
                inDegree[neighbour] -= 1

                if inDegree[neighbour] == 0:
                    q.append(neighbour)
        
        return path if count == numCourses else []