class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # core of the problem: determining maximum number of overlapping intervals at any given point
        
        intervals.sort() # sort by start time
        res = 0  # Count number of overlaps
        pq = []  # Priority queue to track the end time of intervals

        for start, end in intervals:
            # push end time and remove intervals whose end time is earlier than current interval start time, as they no longer overlap with the curret interval
            while pq and start > pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, end)

            # size of current heap tells us max overlapping intervals currently
            res = max(res, len(pq))

        return res