class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # boyer moore majority voting algorithm : O(n) time, O(1) space
        n = len(nums)
        candidate = -1
        votes = 0

        for i in range(n):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if nums[i] == candidate:
                    votes += 1
                else:
                    votes -= 1
        
        # count freq of majority element
        freq = 0
        for num in nums:
            if num == candidate:
                freq += 1
        
        # checking if curr split is valid
        count = 0
        for i in range(n):
            if nums[i] == candidate:
                count += 1
            remaining_count = freq - count
            # check if they are majority elements in each split
            if count * 2 > i + 1 and remaining_count * 2 > n - i - 1:
                return i
        
        return -1