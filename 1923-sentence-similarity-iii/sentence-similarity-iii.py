class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        parts1 = sentence1.split()
        parts2 = sentence2.split()
        
        # parts1 will be the one with lesser words
        if len(parts1) >= len(parts2):
            parts1, parts2 = parts2, parts1

        start, end1, end2 = 0, len(parts1) - 1, len(parts2) - 1

        # Find maximum words matching from the beginning
        while start < len(parts1) and parts1[start] == parts2[start]:
            start += 1
        
        # Find maximum words matching in the end
        while end1 >= 0 and parts1[end1] == parts2[end2]:
            end1 -= 1
            end2 -= 1
        
        # means all words in smaller part found in larger part in order
        return end1 < start