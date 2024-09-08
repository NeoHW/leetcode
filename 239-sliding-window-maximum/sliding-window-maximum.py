class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic decreasing queue
        # max element should be at the front
        res = []
        q = deque()

        # initalise the monotonic decreasing queue
        for i in range(k):
            while q and nums[i] > q[-1]: # while incoming > last elemment in queue
                q.pop() # remove the last element so it will be monotonic decreasing
            q.append(nums[i])
        
        res.append(q[0])
        l,r = 0,k-1

        while r < len(nums)-1:
            # remove max element if it is no longer in window (left)
            if nums[l] == q[0]:
                q.popleft()
            l += 1
            
            # add in right element into montonic decreasing queue 
            r += 1
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            
            res.append(q[0])
        return res
