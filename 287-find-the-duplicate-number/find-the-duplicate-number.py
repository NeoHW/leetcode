class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for each number, change the index that number is pointing to to negative
        for num in nums:
            index = abs(num)

            if nums[index] < 0:
                return index
            
            nums[index] = -nums[index]
        
        return -1
