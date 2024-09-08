class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        hm_s1 = Counter(s1)
        hm_s2 = Counter(s2[:len_s1])

        l = 0

        for r in range(len_s1, len_s2 + 1): # +1 here to do checking for last element too
            if hm_s1 == hm_s2:
                return True

            if r < len_s2:
                hm_s2[s2[l]] -= 1
                if hm_s2[s2[l]] == 0:
                    del hm_s2[s2[l]] # clean up those with 0 freq
                l += 1
                hm_s2[s2[r]] += 1
                
        return False
