class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
        
        pq = [] # min heap of k elements

        for num,freq in hm.items():
            if len(pq) < k:
                heapq.heappush(pq, (freq, num))
            else:
                heapq.heappushpop(pq, (freq, num))
        
        return [num for freq, num in pq]