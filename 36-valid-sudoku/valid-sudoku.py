class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # to see which box
                n = board[r][c]
                area = (r // 3) * 3 + (c // 3)
                if n != '.':
                    if n in row[r] or n in col[c] or n in box[area]:
                        return False
                row[r].add(n)
                col[c].add(n)
                box[area].add(n)
        
        return True