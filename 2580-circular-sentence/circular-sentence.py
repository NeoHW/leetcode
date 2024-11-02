class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        isCircular = True
        
        words = sentence.split()
        start = words[0][0]
        end = words[0][-1]

        for i in range(1, len(words)):
            curr_word = words[i]
            if curr_word[0] != end:
                return False
            end = curr_word[-1]

        return end == start            