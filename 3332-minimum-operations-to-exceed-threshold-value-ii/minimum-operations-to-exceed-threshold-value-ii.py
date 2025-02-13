class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums) 
        res = 0
        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
        
        return res
        