class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # use a frequency array for rows & colums
        # preprocess data (reverse index)

        m,n = len(mat), len(mat[0])
        col_freq = [0] * m
        row_freq = [0] * n
        positions = {}

        # reverse index
        for i in range(m):
            for j in range(n):
                positions[mat[i][j]] = (i,j)
        
        for index, num in enumerate(arr):
            i, j = positions[num]
            col_freq[i] += 1
            row_freq[j] += 1
            if col_freq[i] == n or row_freq[j] == m:
                return index
        
        return