class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []
        for gift in gifts:
            heapq.heappush(pq, -gift)
        
        for i in range(k):
            num = -heapq.heappop(pq)
            heapq.heappush(pq, -int(sqrt(num)))
        
        return -sum(pq)
