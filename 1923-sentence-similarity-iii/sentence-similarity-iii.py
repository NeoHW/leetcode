class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        parts1 = sentence1.split()
        parts2 = sentence2.split()
        
        # parts1 will be the one with lesser words
        if len(parts1) >= len(parts2):
            parts1, parts2 = parts2, parts1

        if len(parts1) == 1:
            return parts1[0] == parts2[0] or parts1[0] == parts2[-1]
        
        # 2 pointers for both sentences
        l1, r1 = 0, len(parts1)-1
        l2, r2 = 0, len(parts2)-1

        while l1 <= r1:
            if parts1[l1] != parts2[l2] and parts1[r1] != parts2[r2]:
                return False
            elif parts1[l1] == parts2[l2] and parts1[r1] == parts2[r2]:
                l1 += 1
                l2 += 1
                r1 -= 1
                r2 -= 1
                continue
            elif parts1[l1] == parts2[l2]:
                l1 += 1
                l2 += 1
            else:
                r1 -= 1
                r2 -= 1
        
        return True