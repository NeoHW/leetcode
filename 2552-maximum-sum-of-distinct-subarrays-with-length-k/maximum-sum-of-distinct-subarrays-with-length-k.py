class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hm = {}
        max_sum = 0
        curr_sum = 0
        
        for i in range(k):
            if nums[i] not in hm:
                hm[nums[i]] = 0
            hm[nums[i]] += 1
            curr_sum += nums[i]
        
        if len(hm) == k:
            max_sum = curr_sum
        
        l = 0
        for r in range(k, len(nums)):
            right_num = nums[r]
            if right_num not in hm:
                hm[right_num] = 0
            hm[right_num] += 1
            curr_sum += right_num
            
            left_num = nums[l]
            if hm[left_num] == 1:
                del hm[left_num]
            else:
                hm[left_num] -= 1
            curr_sum -= left_num
            l += 1


            if len(hm) == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum