class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window of size k
        l, curr = 0,0
        res = float("inf") 

        for i in range(k):
            if blocks[i] == 'W':
                curr += 1
        
        res = curr
        
        for r in range(k, len(blocks)):
            if blocks[l] == 'W':
                curr -= 1

            if blocks[r] == 'W':
                curr += 1

            res = min(res, curr)
            l += 1
        
        return res