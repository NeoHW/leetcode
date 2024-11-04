class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        prev = word[0]
        count = 1

        for i in range(1, len(word)):
            if word[i] != prev:
                if count != 0:
                    comp = comp + str(count) + prev
                prev = word[i]
                count = 0
            
            count += 1
            if count == 9:
                comp = comp + str(count) + prev
                count = 0
            
        if count != 0:
            comp = comp + str(count) + prev
        
        return comp