class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required_letters = defaultdict(int)
        for word in words2:
            hm = Counter(word)
            for letter, count in hm.items():
                if required_letters[letter] < count:
                    required_letters[letter] = count
        
        res = []

        for word in words1:
            hm = Counter(word)
            toAdd = True
            for k, v in required_letters.items():
                if k not in hm or hm[k] < v:
                    toAdd = False
                    break
            if toAdd:
                res.append(word)
        
        return res