class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        curr_rle = "1"
        for i in range(1, n):
            curr_rle = self.getRLE(curr_rle)
        
        return curr_rle
    
    def getRLE(self, s: str) -> str:
        count = 1
        rle = ""
        prev_num = s[0]

        for i in range (1,len(s)):
            curr_num = s[i]
            if prev_num != curr_num:
                rle += str(count) + str(prev_num)
                prev_num = curr_num
                count = 1
            else:
                count += 1
        
        rle += str(count) + str(prev_num)
        return rle
