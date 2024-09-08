class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        have, need = 0, len(count) # need is how many distinct chars we need 
        ans_left_index, ans_right_index, min_length = 0, 0, float('INF')

        curr_window = defaultdict(int) # stores alphabet : count in current window        

        l = 0
        for r in range(len(s)):
            c = s[r]
            curr_window[c] += 1
            if c in count and curr_window[c] == count[c]: # fulfilled requirements for that character
                have += 1

            # update answers while have == need
            while have == need:
                substring_length = r - l + 1
                if substring_length < min_length:
                    min_length = substring_length
                    ans_left_index = l
                    ans_right_index = r
            
                curr_window[s[l]] -= 1
                if s[l] in count and curr_window[s[l]] < count[s[l]]: # requirements now not fulfilled
                    have -= 1
                l += 1
        
        return s[ans_left_index:ans_right_index + 1] if min_length != float('INF') else ""