class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        # find the longest subarray in range (i,j) that  A[j] - A[i] ≤ 2 * k.
        left = 0
        max_window = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            max_window = max(max_window, right - left + 1)

        return max_window