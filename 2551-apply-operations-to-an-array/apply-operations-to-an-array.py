class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_arr = [0] * n
        res_index = 0

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
            if nums[i] != 0:
                res_arr[res_index] = nums[i]
                res_index += 1
        
        # check last index
        if nums[-1] != 0:
            res_arr[res_index] = nums[-1]
        
        return res_arr