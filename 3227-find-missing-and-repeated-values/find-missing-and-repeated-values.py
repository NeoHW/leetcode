class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n_square = n ** 2
        curr_sum = 0
        duplicate_num = 0
        seen = set()

        for row in grid:
            for num in row:
                if num in seen:
                    duplicate_num = num 
                else:
                    curr_sum += num
                    seen.add(num)
        
        expected_sum = (n_square * (n_square + 1)) // 2
        missing_num = expected_sum - curr_sum
        return [duplicate_num, missing_num]