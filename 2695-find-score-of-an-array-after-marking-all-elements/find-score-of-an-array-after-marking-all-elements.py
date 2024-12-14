class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = []
        hs = [0] * len(nums)

        for i,a in enumerate(nums):
            heapq.heappush(pq, (a,i))
        
        score = 0
        while pq:
            num,i = heapq.heappop(pq)
            if hs[i] == 0:
                score += num
                if i-1 >= 0:
                    hs[i-1] = 1
                if i+1 < len(nums):
                    hs[i+1] = 1
        
        return score