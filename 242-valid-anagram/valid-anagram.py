class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = defaultdict(int)

        for c in s:
            hm[c] += 1

        for c in t:
            hm[c] -= 1
        
        for v in hm.values():
            if v != 0:
                return False
        
        return True