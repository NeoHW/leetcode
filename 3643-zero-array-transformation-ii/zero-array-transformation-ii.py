class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # maintain an active set of queries and update nums only when necessary. 
        # a difference array helps us track how nums is being modified

        n = len(nums)
        total_sum = 0 # track the cumulative sum of updates applied up to a given index
        num_queries = 0
        difference_arr = [0] * (n + 1) # to prevent out of bounds access

        for i in range(n):
            # iterate through queries while current index of nums cannot equal zero
            while total_sum + difference_arr[i] < nums[i]:
                num_queries += 1

                if num_queries > len(queries):
                    return -1
                
                left, right, val = queries[num_queries - 1]

                # process start and end of range
                if right >= i: # only apply if range affects current index
                    difference_arr[max(left, i)] += val
                    difference_arr[right + 1] -= val
            
            # update prefix sum at current index
            total_sum += difference_arr[i]
        
        return num_queries