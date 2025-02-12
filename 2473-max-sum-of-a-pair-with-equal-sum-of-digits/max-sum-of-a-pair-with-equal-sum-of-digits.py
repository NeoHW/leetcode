class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hm = defaultdict(list) 

        for num in nums:
            pq = hm[self.sum_digits(num)]
            heapq.heappush(pq, num)
            if len(pq) > 2:
                heapq.heappop(pq)

        res = -1
        for _, pq in hm.items():
            if len(pq) != 2:
                continue
            res = max(res, sum(pq))
        
        return res
    
    def sum_digits(self, n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r