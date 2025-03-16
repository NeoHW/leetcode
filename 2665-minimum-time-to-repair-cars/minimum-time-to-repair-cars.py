class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_time, max_time = 1, max(ranks) * (cars ** 2) 
        res = max_time

        while min_time <= max_time:
            mid = (min_time + max_time) // 2
            if self.canRepair(ranks, cars, mid):
                res = mid 
                max_time = mid - 1
            else:
                min_time = mid + 1 
        
        return res
    
    def canRepair(self, ranks: List[int], cars: int, time: int) -> bool:
        total_repaired = 0
        for rank in ranks:
            total_repaired += int(sqrt(time / rank))
            if total_repaired >= cars:
                return True
        
        return False