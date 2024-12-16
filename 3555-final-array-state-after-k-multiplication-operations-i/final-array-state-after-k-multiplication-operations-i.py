class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))
        
        for _ in range(k):
            num, i = heapq.heappop(pq)
            num *= multiplier
            heapq.heappush(pq, (num, i))
        
        res = [-1] * len(nums)

        for num, i in pq:
            res[i] = num
        
        return res