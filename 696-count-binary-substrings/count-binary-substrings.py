class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        
        # count number of occurances for each grouping of 1 and 0 individually
        # "0110001111" will be [1, 2, 3, 4]
        # for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be minimum of 0 and 1.
        # "0001111" will be min(3,4): as we can only make groups of min number

        counts = []
        curr_count = 1

        for i in range(1,n):
            if s[i] == s[i-1]:
                curr_count += 1
                continue
            counts.append(curr_count)
            curr_count = 1
        counts.append(curr_count) # add in the last count
        

        res = 0
        for i in range(1,len(counts)):
            res += min(counts[i], counts[i-1])
        
        return res
