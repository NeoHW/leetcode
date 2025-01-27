class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # use khan algo and maintain list of dependencies for each node
        prereqs = defaultdict(set)
        AL = defaultdict(list)
        in_degrees = [0] * numCourses

        for v,w in prerequisites:
            AL[v].append(w)
            in_degrees[w] += 1
        
        q = deque()
        for node in range(numCourses):
            if in_degrees[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            for neighbour in AL[node]:
                # add both node and prereqs of node to prereq of neighbour
                prereqs[neighbour].add(node)
                for prereq in prereqs[node]:
                    prereqs[neighbour].add(prereq)

                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    q.append(neighbour)
        
        res = []
        for first,second in queries:
            res.append(first in prereqs[second])
        
        return res