class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])
        l, r = 0, n - 1
        while l <= r:
            mid = (l+r) // 2
            max_row = 0

            for i in range(m):
                max_row = i if (mat[i][mid] >= mat[max_row][mid]) else max_row
            
            is_left_larger = (mid-1 >= l and mat[max_row][mid-1] > mat[max_row][mid])
            is_right_larger = (mid+1 <= r and mat[max_row][mid+1] > mat[max_row][mid])

            if (not is_left_larger) and not (is_right_larger):
                return [max_row, mid]
            elif is_left_larger:
                r = mid - 1
            else:
                l = mid + 1
        
        return [-1, -1]