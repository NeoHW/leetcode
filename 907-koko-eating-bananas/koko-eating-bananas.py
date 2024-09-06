class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # instead of going through the numbers from min to max 1 by 1, we use binary search
        l,r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            
            if self.canFinish(piles, h, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
    
    def canFinish(self, piles:List[int], h:int, k:int) -> bool:
        total_hours = 0
        for p in piles:
            total_hours += (p + k -1 ) // k  # to round up the division
        return total_hours <= h