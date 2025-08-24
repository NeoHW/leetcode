class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = 0
        groups = []

        for num in nums:
            if num == 0:
                groups.append(curr)
                groups.append(0)
                curr = 0
            else:
                curr += 1
        
        # for last group
        groups.append(curr)
        
        # if one group
        if len(groups) == 1:
            return groups[0] - 1

        res = 0
        for i in range(len(groups) - 2):
            if groups[i+1] == 0:
                res = max(res, groups[i] + groups[i+2])
        
        return res
