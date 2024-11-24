class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # if there are even number of -ve, we can transform all of them to +ve
        # if there are odd number of -ve, we just need to make the smallest number -ve
        
        abs_sum = 0
        negative_count = 0
        smallest_abs_seen = float('inf')
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                curr_num = matrix[i][j]
                abs_sum += abs(curr_num)
                if curr_num < 0:
                    negative_count += 1
                smallest_abs_seen = min(smallest_abs_seen, abs(curr_num))
        
        if negative_count % 2 == 0:
            return abs_sum
        
        # we need to deduct smallest_abs_seen twice to account for making it negative
        # e.g. 3 to - 3 is a difference of 6
        return abs_sum - (smallest_abs_seen * 2)