class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len(s1) > len(s2): 
          return False
        
        hm_s1 = defaultdict(int)
        hm_s2 = defaultdict(int)

        # populate hashmap for first window
        for i in range(len_s1):
            hm_s1[s1[i]] += 1
            hm_s2[s2[i]] += 1

        # check first window
        if hm_s1 == hm_s2:
            return True
        
        l = 0
        for r in range(len_s1, len_s2):
            hm_s2[s2[l]] -= 1
            if hm_s2[s2[l]] == 0:
                del hm_s2[s2[l]]
            
            hm_s2[s2[r]] += 1

            if hm_s1 == hm_s2:
                return True
            
            l += 1
                
        return False
