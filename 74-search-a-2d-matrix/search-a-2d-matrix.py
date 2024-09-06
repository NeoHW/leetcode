class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on i, then j
        m,n = len(matrix), len(matrix[0])

        top,btm = 0, m -1
        i = 0

        while top <= btm:
            i = (top + btm) // 2
            if target < matrix[i][0]: 
                btm = i - 1
            elif target > matrix[i][n-1]:
                top = i + 1
            else:
                break
        
        l,r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False