class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i in range(len(words)):
            word = words[i]
            isFound = True
            for j in range(len(searchWord)):
                if len(word) < len(searchWord):
                    isFound = False
                    break
                if searchWord[j] != word[j]:
                    isFound = False
                    break
            
            if isFound:
                return i + 1
        
        return -1
