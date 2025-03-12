class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_count = len(nums) - self.upperBound(nums)
        negative_count = self.lowerBound(nums)
        return max(positive_count, negative_count)

    # returns first index where value >= 0
    def lowerBound(self, nums: List[int]) -> int:
        index = len(nums) # no valid index found
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
                index = mid
        
        return index

    # returns first index where value > 0
    def upperBound(self, nums: List[int]) -> int:
        index = len(nums)
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1
                index = mid
        
        return index
