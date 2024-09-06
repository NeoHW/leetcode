class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        
        # heapq.nlargest(k, iterable, key = func):
        return heapq.nlargest(k, hm.keys(), key = hm.get)
