class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return True
            
            # left sorted portion
            if nums[left] < nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] == nums[mid]:
                left += 1
            else: # right sorted portion
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False
 