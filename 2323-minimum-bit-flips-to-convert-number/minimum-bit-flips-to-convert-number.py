class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        diff = start ^ goal 

        while diff:
            count += diff & 1 # increment count if last bit is 1
            diff >>= 1
        
        return count
        