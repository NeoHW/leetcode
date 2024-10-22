class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # backtracking + hashset
        seen = set()
        return self.backtrack(s,0,seen)
    
    def backtrack(self, s, start_index, seen):
        # base case: processed all chars in the string
        if start_index == len(s):
            return 0
        
        max_count = 0

        for end_index in range(start_index + 1, len(s) + 1):
            sub_string = s[start_index:end_index]

            if sub_string not in seen:
                seen.add(sub_string)
                # explore other splits starting from current end index
                max_count = max(max_count, 1 + self.backtrack(s, end_index, seen))
                seen.remove(sub_string)
        
        return max_count