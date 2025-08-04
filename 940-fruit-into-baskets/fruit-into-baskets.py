class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = defaultdict(int) 
        l = 0
        res = 0

        for r in range(len(fruits)):
            hm[fruits[r]] += 1

            while len(hm) > 2:
                hm[fruits[l]] -= 1
                if hm[fruits[l]] == 0:
                    del hm[fruits[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
