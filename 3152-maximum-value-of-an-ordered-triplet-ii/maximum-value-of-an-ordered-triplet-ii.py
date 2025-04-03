class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num, max_diff, max_triplet = 0, 0, 0 

        for num in nums:
            max_triplet = max(max_triplet, max_diff * num)
            max_diff = max(max_diff, max_num - num)
            max_num = max(max_num, num)
        
        return max_triplet
