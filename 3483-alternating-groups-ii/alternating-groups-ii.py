class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        alternating_count = 1
        prev_colour = colors[0]

        for i in range(1,n + k - 1):
            index = i % n

            if colors[index] == prev_colour:
                alternating_count = 1
                prev_colour = colors[index]
                continue
            
            alternating_count += 1
            if alternating_count >= k:
                res += 1
            prev_colour = colors[index]
        
        return res
