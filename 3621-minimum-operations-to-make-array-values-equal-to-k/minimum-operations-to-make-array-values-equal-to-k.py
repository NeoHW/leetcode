class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # basically return number of distinct elements greater than k
        if min(nums) < k:
            return -1
        
        hs = set()
        for num in nums:
            if num > k:
                hs.add(num)
        
        return len(hs)