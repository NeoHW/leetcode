class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the main idea for our checks is to converge the left and right bounds on the start
        # of the pivot, and never disqualify the index for a possible minimum value.
        l, r = 0, len(nums) -1

        while l < r: # do not use l <= r if not it will loop forever
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # if middle number more than last index, means there is a pivot to the right
                # which is why values wrapped and become smaller
                # so we need to search in the right half
                l = mid + 1
            else:
                # pivot MUST be at mid or left of mid (<= mid)
                # so we do not discard it by doing r = mid -1. it sitll might have minimum value
                r = mid
        
        # left and right would converge to a single index(min value)
        # when shrinking both bounds, it does not disqualify a value
        # this leads to shrinking to just one value, without disqualifying a possible minimum
        return nums[l]