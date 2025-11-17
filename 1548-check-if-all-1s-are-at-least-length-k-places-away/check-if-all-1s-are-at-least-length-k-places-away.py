class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_1 = float("-inf")
        for i, num in enumerate(nums):
            if num == 1:
                if i-last_1 <= k:
                    return False
                last_1 = i
        
        return True