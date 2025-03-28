class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        res = 0

        for row in grid:
            for num in row:
                arr.append(num)
        
        arr.sort()
        n = len(arr)

        median = arr[n // 2]

        for num in arr:
            # check if transformation is possible
            if num % x != median % x:
                return -1
            res += abs(median - num) // x

        return res 