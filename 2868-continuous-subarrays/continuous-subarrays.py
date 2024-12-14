class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # calculate number of valid subarrays ending at right: right - left + 1
        freq_map = {}
        left = right = 0
        count = 0

        for right in range(len(nums)):
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1

            # reduce window by shifting left pointer if condition false
            while max(freq_map) - min(freq_map) > 2:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # add count of all valid subarrays ending at right
            count += right - left + 1

        return count