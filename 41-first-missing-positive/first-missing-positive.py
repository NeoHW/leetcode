class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Pass 1: Replace all negative numbers and out-of-range numbers (> n) with a placeholder value (n + 1).
        # Why? Because the first missing positive number must be in the range [1, n],
        # so numbers ≤ 0 or > n are irrelevant and can be ignored.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Pass 2: similar idea to LC find duplicate number
        # Mark the presence of numbers in the range [1, n] using index-based marking.
        # We use negation as a marker to indicate a number is present in the array.
        for num in nums:
            num = abs(num)
            if 1 <= num <= n:
                index = num - 1 # convert to 0 based index
                if nums[index] > 0: # mark if positive
                    nums[index] = -nums[index]

        # Pass 3: The first index where the value is still positive means the number (index + 1) is missing.
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1