class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # line sweep algorithm

        if len(nums) == 1:
            return 1
        
        max_value = max(nums)
        count = [0] * (max_value + 1)

        # Increment at the start of the range
        for num in nums:
            count[max(0, num - k)] += 1 # Increment at the start of the range
            if num + k + 1 <= max_value:
                count[num + k + 1] -= 1 # Decrement after the range
            
        max_beauty = 0
        current_sum = 0

        for val in count:
            current_sum += val
            max_beauty = max(max_beauty, current_sum)

        return max_beauty