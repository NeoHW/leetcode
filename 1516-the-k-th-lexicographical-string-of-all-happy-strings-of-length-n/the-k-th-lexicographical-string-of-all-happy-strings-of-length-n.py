class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        hs = set()
        letters = ['a','b','c']
        self.backtrack(n,"",hs,letters,-1)

        if len(hs) < k:
            return ""

        hs_list = list(hs)
        hs_list.sort()
        return hs_list[k-1]

    def backtrack(self, n: int, s:str, hs:set, letters: list, prev_index: int):
        if len(s) == n:
            hs.add(s)
            return
        
        for i in range(len(letters)):
            if i == prev_index:
                continue
            self.backtrack(n, s + letters[i], hs, letters, i)