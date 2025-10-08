class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # takes the first one that ends first
        intervals.sort(key=lambda x:x[1])
        res = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                res += 1
            else:
                prev_end = end
        
        return res