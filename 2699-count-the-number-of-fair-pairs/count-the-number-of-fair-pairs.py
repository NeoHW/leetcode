class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # we can sort the array
        # main idea: count pairs with sum <= upper, 
        # then subtract total pairs with sum < lower

        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    # counts number of pairs (i < j) with nums[i] + nums[j] < value
    def lower_bound(self, nums: List[int], value: int) -> int:
        n = len(nums)
        count = 0
        l, r = 0, n-1
        while l < r:
            if nums[l] + nums[r] < value:
                # If nums[l] + nums[r] <= value, then for this l,
                # all indices k from l+1..r also satisfy nums[l]+nums[k] ≤ value
                count += (r - l)
                l += 1
            else:
                # sum too big, decrease r to reduce the sum
                r -= 1
        return count