class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        freq = defaultdict(int)
        left = 0
        current_pairs = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            current_pairs += freq[nums[right]] - 1

            while current_pairs >= k:
                count += len(nums) - right
                freq[nums[left]] -= 1
                current_pairs -= freq[nums[left]]
                left += 1
        
        return count
