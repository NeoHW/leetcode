class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        hm = {} # tracks the mapping of vowels to count
        res = 0
        num_const = 0
        l,r = 0,0

        next_const = [0] * n # an array to keep track of what is the index of the next const from that index
        next_const_index = n

        # work backwards to find out what the next const index for each char
        for i in range(n-1, -1, -1):
            next_const[i] = next_const_index
            if word[i] not in vowels:
                next_const_index = i

        while r < n:
            end_letter = word[r]
            if end_letter in vowels:
                hm[end_letter] = hm.get(end_letter, 0) + 1
            else:
                num_const += 1
            
            while num_const > k:
                start_letter = word[l]
                if start_letter in vowels:
                    hm[start_letter] -= 1
                    if hm[start_letter] == 0:
                        del hm[start_letter]
                else:
                    num_const -= 1
                l += 1
            
            # adjusting substring by expanding/shrinking to find more valid substrings
            while (l < n and len(hm) == 5 and num_const == k):
                # add in number of valid substrings with the given start 
                res += next_const[r] - r

                # find more valid substrings by shrinking window until no more valid substring
                start_letter = word[l]
                if start_letter in vowels:
                    hm[start_letter] -= 1
                    if hm[start_letter] == 0:
                        del hm[start_letter]
                else:
                    num_const -= 1
                l += 1
            
            r += 1
                    
        return res