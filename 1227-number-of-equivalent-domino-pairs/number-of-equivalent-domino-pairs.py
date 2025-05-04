class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hm = {}
        for domino in dominoes:
            x,y = domino
            if x > y:
                x,y = y,x
            
            if (x,y) not in hm:
                hm[(x,y)] = 0
            
            hm[(x,y)] += 1
        
        res = 0
        for v in hm.values():
            res += (v * (v-1)) // 2
        
        return res