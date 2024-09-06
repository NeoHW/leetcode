class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        
        # heapq.nlargest(k, iterable, key = func):
        return heapq.nlargest(k, hm.keys(), key = hm.get)

        # under the hood it is 
        pq = []
        for num, freq in hm.items():
            # maintain a pq of size k
            if len(pq) < k:
                heapq.heappush(pq, (freq,num))
            else:
                heapq.heappushpop(pq, (freq, num))
        
        return [num for freq, num in pq]