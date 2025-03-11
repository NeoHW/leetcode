class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # pass 1: convert all negative & out of size numbers to 0, as that means invalid
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # pass 2: similar idea to LC find duplicate number
        for num in nums:
            num = abs(num)
            if 1 <= num <= n:
                index = num - 1 # convert to 0 based index
                if nums[index] > 0: # mark if positive
                    nums[index] = -nums[index]

        # pass 3: the first index that has a number that is not negative is missing
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1