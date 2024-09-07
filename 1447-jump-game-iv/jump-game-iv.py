class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        # build a graph (dict of value: list of indexes)
        hm = defaultdict(list)
        for i,a in enumerate(arr):
            hm[a].append(i)

        # do our bfs from index 0
        q = deque()
        q.append(0)

        steps = 0
        while q:
            for _ in range(len(q)):
                curr_index = q.popleft()

                if curr_index == n - 1:
                    return steps
                
                # we can move to i-1, i+1 or any other index of current number
                # check if visited those indexes yet (the key stil in hashmap)
                if curr_index -1 >= 0 and arr[curr_index-1] in hm:
                    q.append(curr_index-1)
                
                if curr_index + 1 < n and arr[curr_index+1] in hm:
                    q.append(curr_index+1)
                
                for neighbour in hm[arr[curr_index]]:
                    if neighbour != curr_index:
                        q.append(neighbour)
                
                # remove current index value of array from hashmap to prevent revisitng
                del hm[arr[curr_index]]
            steps += 1

        return steps
