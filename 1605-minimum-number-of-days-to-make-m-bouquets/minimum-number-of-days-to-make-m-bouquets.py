class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 0, max(bloomDay) # right bound is longest day to bloom
        min_days = -1

        if len(bloomDay) < m*k:
            return min_days

        while l <= r:
            mid = (l + r) // 2
            bouquests = self.calculate_bouquets_in_day(mid, bloomDay, k)
            if bouquests >= m:
                min_days = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_days 
    
    def calculate_bouquets_in_day(self, day, bloomDay, k):
        bouquets, count = 0, 0
        for f in bloomDay:
            if f <= day:
                count += 1
            else:
                count = 0
            
            if count == k:
                bouquets += 1
                count = 0 
                
        return bouquets