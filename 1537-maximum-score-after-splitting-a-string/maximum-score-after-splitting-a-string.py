class Solution:
    def maxScore(self, s: str) -> int:
        # score = num_zeros in left + num_ones in right
        # num_ones in right = total num_ones - nums_one seen in left

        counts = Counter(s)
        num_ones = counts["1"]
        max_score = 0
        seen_ones, seen_zeros = 0, 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                seen_ones += 1 
            else:
                seen_zeros += 1
            
            curr_score = seen_zeros + (num_ones - seen_ones)
            max_score = max(max_score, curr_score)
        
        return max_score
