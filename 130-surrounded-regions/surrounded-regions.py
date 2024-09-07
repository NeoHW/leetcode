class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # anything connected to the borders would not be captured
        m,n = len(board), len(board[0])
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()

        def dfs(i, j):
            if i not in range(m) or j not in range(n) or board[i][j] != "O" or (i,j) in visited:
                return
            visited.add((i,j))
            for dx,dy in dir:
                dfs(i + dx, j + dy)

        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    if board[i][j] == "O":
                        dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"