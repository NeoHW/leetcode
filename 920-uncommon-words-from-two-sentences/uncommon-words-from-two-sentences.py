class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        parts1 = s1.split(" ")
        parts2 = s2.split(" ")
        
        hs1 = Counter(parts1)
        hs2 = Counter(parts2)
        res = []

        for word,count in hs1.items():
            if count == 1 and word not in hs2:
                res.append(word)

        for word,count in hs2.items():
            if count == 1 and word not in hs1:
                res.append(word)
        
        return res