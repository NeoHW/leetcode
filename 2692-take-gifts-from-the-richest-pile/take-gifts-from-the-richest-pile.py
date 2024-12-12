class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = [-gift for gift in gifts]
        heapq.heapify(pq)
        
        for _ in range(k):
            num = -heapq.heappop(pq)
            heapq.heappush(pq, -int(sqrt(num)))
        
        return -sum(pq)
