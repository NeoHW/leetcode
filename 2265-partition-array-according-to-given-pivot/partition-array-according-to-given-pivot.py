class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # we cannot use DNF as DNF is not a stable sort
        n = len(nums)
        low, high = 0 , len(nums) - 1
        pivot_index = 0
        res = [0] * n

        for i in range(n):
            if nums[i] < pivot:
                res[low] = nums[i]
                low += 1
        
        for j in range(n-1, -1, -1):
            if nums[j] > pivot:
                res[high] = nums[j]
                high -= 1
        
        while low <= high:
            res[low] = pivot
            low += 1
        
        return res
