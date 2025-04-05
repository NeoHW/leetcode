class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(nums, index, curr_subset, subsets):
            if index == len(nums):
                subsets.append(curr_subset.copy())
                return
            
            # include curr index
            curr_subset.append(nums[index])
            dfs(nums, index + 1, curr_subset, subsets)

            # dont include curr index
            curr_subset.pop()
            dfs(nums, index + 1, curr_subset, subsets)
        
        subsets = []
        dfs(nums, 0, [], subsets)

        total_sum = 0
        for subset in subsets:
            curr_sum = 0
            for num in subset:
                curr_sum ^= num
            total_sum += curr_sum
        
        return total_sum